import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame as df

df = pd.read_csv('C:\Python35\workspace\In-Class_network.txt',sep = '\t').iloc[0:,:-5]

def from_in_class_network(G): #3a
    nx.draw(G, node_color = '#00BBFF', node_size = 25)
    plt.show()
    
idd = df['ID']
ids = df['IDs-of-acquaintances']

idss = []
for i in range(len(ids)):
    idss.append(ids[i].split(","))

idsss = []
for i in range(len(idss)):
    for j in range(len(idss[i])):
        idsss.append(idss[i][j])

nw = []
for i in range(len(idsss)):
    if idsss[i] == ' ':
         nw.append(100)
    else:
         nw.append(int(idsss[i]))

edge = []
for i in range(len(idd)):
    for j in range(len(ids[i].split(","))):
        edge.append([idd[i],ids.values[i].split(",")[j]])

iddd = []
for i in range(len(edge)):
    iddd.append(edge[i][0])

edge1 = []
for i in range(len(iddd)):
    edge1.append((iddd[i],nw[i]))

G = nx.Graph()
#G.add_nodes_from(edge1)
G.add_edges_from(edge1)
G.to_undirected()

G.remove_node(100)

nod = list(G.nodes())

nnodes = G.order()
nedges = G.size()
deg = G.degree()
avgdeg = np.mean(list(dict(deg).values()))


H = nx.path_graph(G) #3b(iv)

cc = nx.connected_components(G)
lcc = max(nx.connected_components(G),key = len)

def degree_dist():
        
    k = []
    for i in range(len(nod)):
        k.append(G.degree(nod[i]))
    
    return k
    
k = degree_dist()

nG = sum(k)/max(k)

lkp = [] #3d
for i in range(len(k)):
    lkp.append(k[i]/sum(k))

pk = []
for i in range(len(idd)):
    pk.append((nod[i],lkp[i]))

def compute_num_triangles(a):  #3e
    
    tri = nx.triangles(a)
    
    return tri
