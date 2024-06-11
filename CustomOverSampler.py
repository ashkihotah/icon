from imblearn.over_sampling import RandomOverSampler, SMOTE

class CustomOverSampler():

    # def __init__(self, condition, true_block):
    #     self.condition = condition
    #     self.true_block = true_block

    def __init__(self, threshold):
        self.threshold = threshold

    def fit_resample(self, X, y):
        y = list(y)
        seed = 42
        occurrences = {item: y.count(item) for item in y}
        min_samples = {}
        for target in occurrences.keys():
            if occurrences[target] < self.threshold:
                min_samples[target] = self.threshold
        ros = RandomOverSampler(sampling_strategy=min_samples, random_state=seed, shrinkage=0)
        return ros.fit_resample(X, y)