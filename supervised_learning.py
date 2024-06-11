from operator import itemgetter
from lightgbm import LGBMClassifier
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn.calibration import LabelEncoder
from sklearn.discriminant_analysis import StandardScaler
from sklearn.ensemble import GradientBoostingClassifier, HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, average_precision_score, balanced_accuracy_score, f1_score, make_scorer, precision_score, recall_score
from sklearn.model_selection import GridSearchCV, StratifiedKFold, cross_val_score, cross_validate, learning_curve, train_test_split
from sklearn.naive_bayes import CategoricalNB, LabelBinarizer, MultinomialNB
from sklearn.neural_network import MLPClassifier
# from sklearn.pipeline import Pipeline
from imblearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
from CustomOverSampler import CustomOverSampler
from preprocessing import getDataset, filter
from imblearn.metrics import geometric_mean_score
from imblearn.over_sampling import RandomOverSampler, SMOTE, ADASYN, BorderlineSMOTE
from imblearn.under_sampling import RandomUnderSampler
from imblearn.combine import SMOTEENN, SMOTETomek

X, y = getDataset(paths = ['./OU Teams/original/gen5ou.json'])

scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

le = LabelEncoder()
le.fit(y)
y = le.transform(y)

def evaluations(clf, X_test, Y_test, cv, log_file): 

    print("{:<25}{:<25}{:<25}{:<25}".format("Metric", "Score Mean", "Score Variance", "Score Std"))
    log_file.write("{:<25}{:<25}{:<25}{:<25}\n".format("Metric", "Score Mean", "Score Variance", "Score Std"))

    metrics = {'Accuracy': make_scorer(accuracy_score),
               'Balanced Accuracy': make_scorer(balanced_accuracy_score),
               'Geometric Mean': make_scorer(geometric_mean_score, average='macro'),
               'Average Precision': make_scorer(average_precision_score, response_method='predict_proba'),
               'Precision': make_scorer(precision_score, average='macro', zero_division=0),
               'Recall': make_scorer(recall_score, average='macro'),
               'F1': make_scorer(f1_score, average='macro')}
    # d = cross_validate(clf, X_test, Y_test, scoring=['accuracy', 'balanced_accuracy', 'average_precision'], cv=cv, n_jobs=-1)
    d = cross_validate(clf, X_test, Y_test, scoring=metrics, cv=cv, n_jobs=-1)

    for key, scores in d.items():
        if 'test_' in key:
            metric_name = key[5:]
            mean = np.mean(scores)
            var = np.var(scores)
            std = np.std(scores)
            print("{:<25}{:<25}{:<25}{:<25}".format(metric_name, str(mean), str(var), str(std)))
            log_file.write("{:<25}{:<25}{:<25}{:<25}\n".format(metric_name, str(mean), str(var), str(std)))

def runExperiment(hyperParameters, classifier, classifierName, suffix, pre_pipeline, seed=42):

    with open('./logs/log_'+classifierName+suffix+'.txt', 'w', encoding='utf-8') as log_file:
        
        cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)
        
        gridSearchCV = GridSearchCV(
            Pipeline(pre_pipeline + [(classifierName, classifier)]),
            param_grid = hyperParameters,
            cv = cv,
            n_jobs = -1,
            scoring = "accuracy"
        )

        # X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=seed)
        # clf = classifier.fit(X_train, Y_train)

        gridSearchCV.fit(X, y)
        clf = gridSearchCV.best_estimator_
        print(gridSearchCV.best_params_)
        log_file.write(str(gridSearchCV.best_params_)+'\n')

        # print("Best Estimator Train Accuracy: ", clf.score(X_train, Y_train))
        # log_file.write("Best Estimator Train Accuracy: "+str(clf.score(X_train, Y_train))+'\n')
        evaluations(clf, X, y, cv, log_file)

        train_sizes, train_scores, test_scores = learning_curve(clf, X, y, cv=cv, scoring='accuracy', random_state=seed)

        print("\n{:<8}{:<25}{:<25}{:<25}{:<25}".format("Size", "Mean Train Score", "Variance Train Score", "Std Train Score", "Train Scores"))
        log_file.write("\n{:<8}{:<25}{:<25}{:<25}{:<25}\n".format("Size", "Mean Train Score", "Variance Train Score", "Std Train Score", "Train Scores"))
        for i in range(0, len(train_scores)):
            mean = np.mean(train_scores[i])
            var = np.var(train_scores[i])
            std = np.std(train_scores[i])
            print("{:<8}{:<25}{:<25}{:<25}{:<25}".format(str(i), str(mean), str(var), str(std), str(train_scores[i])))
            log_file.write("{:<8}{:<25}{:<25}{:<25}{:<25}\n".format(str(i), str(mean), str(var), str(std), str(train_scores[i])))

        print("\n{:<8}{:<25}{:<25}{:<25}{:<25}".format("Size", "Mean Test Score", "Variance Test Score", "Std Test Score", "Test Scores"))
        log_file.write("\n{:<8}{:<25}{:<25}{:<25}{:<25}\n".format("Size", "Mean Test Score", "Variance Test Score", "Std Test Score", "Test Scores"))
        for i in range(0, len(test_scores)):
            mean = np.mean(test_scores[i])
            var = np.var(test_scores[i])
            std = np.std(test_scores[i])
            print("{:<8}{:<25}{:<25}{:<25}{:<25}".format(str(i), str(mean), str(var), str(std), str(test_scores[i])))
            log_file.write("{:<8}{:<25}{:<25}{:<25}{:<25}\n".format(str(i), str(mean), str(var), str(std), str(test_scores[i])))

        mean_train_errors = 1 - np.mean(train_scores, axis=1)
        mean_test_errors = 1 - np.mean(test_scores, axis=1)
        plt.figure()
        plt.plot(train_sizes, mean_train_errors, 'o-', color='r', label='Training Error')
        plt.plot(train_sizes, mean_test_errors, 'o-', color='g', label='Validation Error')
        plt.xlabel('Training examples')
        plt.ylabel('Mean Error')
        plt.legend(loc='best')
        plt.title(classifierName+suffix + ' Learning Curves')
        plt.savefig('./plots/learning_curve_'+classifierName+suffix+'.png')

seed = 42

DTHyperparameters = {
    "DT__criterion": ["gini", "entropy", "log_loss"],
    "DT__max_depth": [10, 20, 40],
    "DT__min_samples_split": [2, 5, 10, 15],
    "DT__min_samples_leaf": [1, 2, 5, 10, 15],
    # "DT__min_weight_fraction_leaf": [1.0],
    # "DT__max_features": [1],
    # "DT__max_leaf_nodes": [5, 10, 15, 20, 25, 30, 40]
    # "DT__min_impurity_decrease": [.1, .05, .005, .0005],
    "DT__class_weight": [None, "balanced"],
    # "DT__ccp_alpha": [0.1, 0.2, 0.4, 0.8],
    # "DT__monotonic_cst": []
    "DT__random_state": [seed]
}

RFHyperparameters = {
    'RF__n_estimators': [100, 200],
    'RF__criterion': ['gini', 'entropy', 'log_loss'],
    'RF__max_depth': [None, 10, 20, 40],
    'RF__class_weight': [None, 'balanced'],
    # 'RF__min_samples_split': [2, 5, 10],
    # 'RF__min_samples_leaf': [1, 2, 4],
    # 'RF__max_features': ['auto', 'sqrt', 'log2'],
    # 'RF__bootstrap': [True, False]
    "RF__random_state": [seed]
}

LGBMHyperparameters = {
    "LGBM__learning_rate": [0.01, 0.05, 0.1, 1.0],
    "LGBM__max_depth": [10, 20, 40],
    "LGBM__n_estimators": [50, 100, 200],
    'LGBM__class_weight': [None, 'balanced'],
    # "LGBM__lambda": [0.01, 0.1, 0.5],
    # "LGBM__num_leaves": [5, 15],
    # "LGBM__min_gain_to_split": [0.1],
    "LGBM__verbose": [-1],
    "LGBM__random_state": [seed]
}

LRHyperparameters = {
    "LR__penalty": ['l1', 'l2', 'elasticnet'],
    "LR__class_weight": [None, 'balanced'],
    'LR__max_iter': [100, 1000],
    "LR__random_state": [seed]
}

MLPHyperparameters = {
    "MLP__verbose": [False],
    "MLP__solver": ['lbfgs', 'adam', 'sgd'],
    "MLP__activation": ['relu', 'logistic', 'tanh'],
    "MLP__early_stopping": [True],
    "MLP__validation_fraction": [0.1, 0.2],
    "MLP__tol": [0.1, 0.01, 0.001],
    "MLP__alpha": [1.0, 0.1, 0.01],
    "MLP__hidden_layer_sizes": [(300, 296)],
    "MLP__max_iter": [1000],
    "MLP__random_state": [seed]
}

GradientBoostedTreeHyperparameters = {
    'GradientBoostedTree__learning_rate': [1.0, 0.5, 0.1],
    'GradientBoostedTree__max_depth': [10, 20, 40],
    # 'RandomForest__min_samples_split': [2, 5, 10],
    # 'RandomForest__min_samples_leaf': [1, 2, 4],
    # 'GradientBoostedTree__max_iter': [20, 50, 100]
    "GradientBoostedTree__random_state": [seed]
}

XGBClassifierHyperparameters = {
    'XGBClassifier__learning_rate': [0.01, 0.05, 0.10],
    'XGBClassifier__max_depth': [10, 20, 40],
    'XGBClassifier__n_estimators': [20, 50, 100],
    'XGBClassifier__lambda': [0.01, 0.1, 0.5],
    "XGBClassifier__random_state": [seed]
}

NaiveBayesHyperparameters = {
    'NaiveBayes__alpha': [1.0]
}

# TECNICHE DI OVER-SAMPLING
cos_30 = CustomOverSampler(threshold=25)
ros = RandomOverSampler(sampling_strategy='not majority', random_state=seed, shrinkage=0)
smote = SMOTE(sampling_strategy='not majority', random_state=seed, k_neighbors=5)
# smoten = SMOTEN(sampling_strategy='not majority', random_state=seed, k_neighbors=5)
# b_smote = BorderlineSMOTE(sampling_strategy='not majority', random_state=seed, k_neighbors=5, kind='borderline-2')
# svm_smote = SVMSMOTE(sampling_strategy='not majority', random_state=seed, k_neighbors=5)
# kmeans_smote = KMeansSMOTE(sampling_strategy='not majority', random_state=seed, k_neighbors=5)
# adasyn = ADASYN(sampling_strategy='not majority', random_state=seed, n_neighbors=5)

# TECNICHE DI UNDER-SAMPLING
rus = RandomUnderSampler(random_state=seed, replacement=True)

#TECNICHE MISTE DI UNDER/OVER-SAMPLING
# smoteen = SMOTEENN(sampling_strategy='not majority', random_state=seed)
smotetomek = SMOTETomek(sampling_strategy='not majority', random_state=seed)

pre_pipelines = [
                 [],                                                            # no sampling
                #  [('RandomOverSampler', ros)],                                # over-sampling
                #  [('CustomOverSampler', cos_30), ('SMOTE', smote)],           # over-sampling
                # #  [('CustomOverSampler', cos_30), ('BSMOTE', b_smote)],        # over-sampling
                # #  [('CustomOverSampler', cos_30), ('SVMSMOTE', svm_smote)],    # over-sampling
                # #  [('CustomOverSampler', cos_30), ('KMSMOTE', kmeans_smote)],  # over-sampling
                # #  [('CustomOverSampler', cos_30), ('ADASYN', adasyn)],         # over-sampling
                #  [('RandomUnderSampler', rus)],                               # under-sampling
                # #  [('CustomOverSampler', cos_30), ('SMOTEENN', smoteen)],      # miste
                #  [('CustomOverSampler', cos_30), ('SMOTETomek', smotetomek)]  # miste
                 ]

for ppln in pre_pipelines:
    if len(ppln) > 0:
        suffix = '_' + ppln[-1][0]
    else:
        suffix = '_noSampling'
    # runExperiment(LRHyperparameters, LogisticRegression(multi_class='multinomial'), 'LR', suffix, pre_pipeline=ppln)
    runExperiment(DTHyperparameters, DecisionTreeClassifier(), 'DT', suffix, pre_pipeline=ppln)
    runExperiment(RFHyperparameters, RandomForestClassifier(), 'RF', suffix, pre_pipeline=ppln)
    runExperiment(LGBMHyperparameters, LGBMClassifier(verbose=-1), 'LGBM', suffix, pre_pipeline=ppln)
    runExperiment(MLPHyperparameters, MLPClassifier(), 'MLP', suffix, pre_pipeline=ppln)

    # runExperiment(GradientBoostedTreeHyperparameters, GradientBoostingClassifier(), 'GradientBoostedTree')
    # runExperiment(XGBClassifierHyperparameters, XGBClassifier(), 'XGBClassifier')
    # runExperiment(NaiveBayesHyperparameters, CategoricalNB(), 'NaiveBayes')