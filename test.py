from networkie.utils.Measures import compute_num_triangles 
import networkx as nx

from networkie.gen.Custom import LoadFromFile as lf
from networkie.utils.Measures import Node 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


print("3A:")
L = lf()
G = L.from_in_class_network()
print(G.edges())



print("3B1:")
print("\tnodes:" , G.number_of_nodes())  # Ex3-2 : 73
print("3B2:")
print("\tedge:%d "%(G.number_of_edges()))  # Ex3-2 : 109
deg_ctr = 0
for i in G.nodes:
    deg_ctr = deg_ctr + G.degree(i)
print("3B3:")
print("\tavg. deg:",deg_ctr/G.number_of_nodes()) #Ex3-2 :2.986 
Gc = max(nx.connected_component_subgraphs(G), key=len)
print("3B4. ??\t")
print("3B5:")
print("\tlargest component size: ",Gc.size())   #Ex3-2 :70
print("3C:")
N = G.number_of_nodes()
E_max = N*(N-1)/2
print("\t",G.number_of_edges()/E_max)



print("3D:\n")
node = Node()
deg = []
idx = []
print(node.degree_dist(G))
deg = node.degree_dist(G)
for i in G.nodes:
    idx.append(i)
data_dict={
    "deg":deg,
    "idx":idx  
    }
df = pd.DataFrame(data_dict,index=deg)

sns.barplot(x="idx",y="deg",data=df)
plt.show()

print("3E:")
compute_num_triangles(G)


