import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations as combos
'''-----------import packages-----------'''

'''-----------read graph from txt file-----------'''
g = nx.Graph() # initialize a graph g
df = pd.read_csv('In-class_network.txt',delimiter="\t") # using pandas's DataFrame to store the info of graph.
df.drop(df.columns[6],axis=1,inplace=True) # drop the last column coming from nowhere.
df['IDs-of-acquaintances'][df['IDs-of-acquaintances'] == ' '] = '999' # set the absent value in 'IDs-of-acquaintances' to be '999'.

'''-----------making dict for nodes & edges-----------'''
d = df.set_index('ID')['IDs-of-acquaintances'].to_dict() # combine 'ID' and 'IDs-of-acquaintances' and form a dict.
d = {k: v.split(',') for k, v in d.items()} # change the value from string to list.
d = {k: [int(i) for i in v] for k, v in d.items()} # change the value from string to integer.

# g.add_nodes_from(d.keys()) # adding nodes for graph g.
# g.remove_node('999')
for k, v in d.items():
	# if v != 999: # discard the absent value in 'IDs-of-acquaintances'.
	g.add_edges_from(([(k, t) for t in v])) # adding edges for graph g.
g.remove_node(999)

#print(nx.info(g))
d2 = nx.to_dict_of_lists(g)
def P3_d():
	global d2
	deg_list=[0] * 75
	for k, v in d2.items():
		deg_list[k] = len(v)
	return deg_list