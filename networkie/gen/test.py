import networkx as nx
from Custom import LoadFromFile as lf
import pandas as pd
import seaborn as sns
path_utils = "/home/james/stat/networkie/networkie/utils/Measures.py"
from import Node 

L = lf()

print("3A:\n")

G = L.from_in_class_network()
print(G.edges())
print("3B:\n")

print("edge:",G.number_of_edges())  # Ex3-2 : 109 
print("nodes:" , G.number_of_nodes())  # Ex3-2 : 73

deg_ctr = 0
for i in G.nodes:
    deg_ctr = deg_ctr + G.degree(i)

print("avg. deg:",deg_ctr/G.number_of_nodes()) #Ex3-2 :2.986 

Gc = max(nx.connected_component_subgraphs(G), key=len)

print("b-4. 看不懂")

print("largest component size: ",Gc.size())   #Ex3-2 :70

print("C:\n")
N = G.number_of_nodes()
E_max = N*(N-1)/2
print(E_max)
print(G.number_of_edges()/E_max)

print("D:\n")


idx = []
deg = []


for i in G.nodes:
    idx.append(i)
    deg.append(G.degree(i))
    
print(idx)
print(deg)

df = pd.DataFrame(idx,index=deg)
print(df)



