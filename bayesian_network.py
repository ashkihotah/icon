import pickle
import time

import networkx as nx
import pandas as pd
from matplotlib import pyplot as plt
from pgmpy.estimators import MaximumLikelihoodEstimator, HillClimbSearch, BayesianEstimator
from pgmpy.inference import VariableElimination
from pgmpy.metrics import correlation_score, log_likelihood_score
from pgmpy.models import BayesianNetwork
from sklearn.metrics import balanced_accuracy_score

from sklearn.preprocessing import LabelEncoder

from preprocessing import getDataset, getSimplifiedDataset, getTypesList

pd.set_option('display.max_columns', 100)
label_encoder = LabelEncoder()

def plotBayesianNetwork(bn: BayesianNetwork):
    G = nx.MultiDiGraph(bn.edges())
    pos = nx.spring_layout(G, iterations=100, k=2,
                           threshold=5, pos=nx.spiral_layout(G))
    nx.draw_networkx_nodes(G, pos, node_size=250, node_color="#ff574c")
    nx.draw_networkx_labels(
        G,
        pos,
        font_size=10,
        font_weight="bold",
        clip_on=True,
        horizontalalignment="center",
        verticalalignment="bottom",
    )
    nx.draw_networkx_edges(
        G,
        pos,
        arrows=True,
        arrowsize=8,
        arrowstyle="->",
        edge_color="blue",
        connectionstyle="arc3,rad=0.2",
        min_source_margin=1.2,
        min_target_margin=1.5,
        edge_vmin=2,
        edge_vmax=2,
    )

    plt.title("Bayesian Network Graph")
    plt.show()
    plt.clf()

def printCPD(bn: BayesianNetwork):
    for cpd in bn.get_cpds():
        print(f'CPD of {cpd.variable}:')
        print(cpd, '\n')

def createBayesianNetwork(dataSet):
    edges = []
    for col in dataSet.columns:
        if 'move' in col:
            edges.append((col.split('_')[0] + '_types', col))
        elif col != 'Target':
            edges.append(('Target', col))
    
    # TROPPO PESANTE COMPUTAZIONALMENTE
    # hc_k2 = HillClimbSearch(dataSet)
    # k2_model = hc_k2.estimate(scoring_method='k2score', max_iter=100)
    # edges = k2_model.edges()

    bn = BayesianNetwork(edges)
    bn.fit(dataSet,estimator=MaximumLikelihoodEstimator,n_jobs=-1)
    with open('./bn_results/bayesian_network.pkl', 'wb') as output:
        pickle.dump(bn, output)
    return bn

def loadBayesianNetwork():
    with open('./bn_results/bayesian_network.pkl', 'rb') as input:
        model = pickle.load(input)
    return model

def generateRandomExample(bn: BayesianNetwork):
    return bn.simulate(n_samples=1)#.drop(columns=['Target'])

def execute_and_print_query(inference, variables, evidence=None, elimination_order="MinFill", show_progress=False):
    start_time = time.time()
    print(inference.query(variables=variables,
                            evidence=evidence,
                            elimination_order=elimination_order,
                            show_progress=show_progress))
    print(f'Query executed in {time.time() - start_time:0,.4f} seconds\n')

column_names = ['Pk1_types', 'Pk2_types', 'Pk3_types', 'Pk4_types', 'Pk5_types',
                'Pk1_move1_type', 'Pk1_move2_type', 'Pk1_move3_type', 'Pk1_move4_type',
                'Pk2_move1_type', 'Pk2_move2_type', 'Pk2_move3_type', 'Pk2_move4_type',
                'Pk3_move1_type', 'Pk3_move2_type', 'Pk3_move3_type', 'Pk3_move4_type',
                'Pk4_move1_type', 'Pk4_move2_type', 'Pk4_move3_type', 'Pk4_move4_type',
                'Pk5_move1_type', 'Pk5_move2_type', 'Pk5_move3_type', 'Pk5_move4_type',
                'Target']

x, y = getSimplifiedDataset(paths = ['./OU Teams/original/gen5ou.json'])
dataset = []
for i in range(len(x)):
    dataset.append(x[i] + [y[i]])

df = pd.DataFrame(dataset, columns=column_names)
print(df)
# bn = createBayesianNetwork(df)


bn = loadBayesianNetwork()
plotBayesianNetwork(bn)
printCPD(bn)
example = generateRandomExample(bn)
print("Esempio randomico:")
print(example)

inference = VariableElimination(bn)
execute_and_print_query(inference, variables=['Pk1_types'], evidence={'Target': 'Bug Fire'})
execute_and_print_query(inference, variables=['Pk1_move1_type'], evidence={'Pk1_types': 'Water_null_type'})