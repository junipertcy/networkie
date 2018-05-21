import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
def compute_num_triangles(G):  # This is Prob. 3-e.
    '''
    Check each node in the graph:
        1.Choosing one node called "i"
        2.Recording the neighbors of node "i" called vector "cmp_l". 
        3.Recording the neighbors of node "j" in cmp_l called vector "G[j].keys()"
        4.Check whether there exists any node in cmp_l and G[j].keys()
             Existing -> tri_ctr + 1
             Not Existing -> Do nothing
        5.return tri_ctr/6 -> Because each traingle would be counted 6 times by rule (4) 
    '''
    

    
    tri_ctr = 0
    for i in G.nodes:
        #print("Node",i,":")
        l = list(G[i].keys())
        cmp_l = list(l)
        #print(cmp_l)
        for j in l:
            cmp_l.remove(j)
            #print("rm: ",cmp_l)
            #print(j)
            #print(list(G[j].keys()))
            common = set(cmp_l) & set(list(G[j].keys()))
            #print(common)
            #print(">> ",len(common))
            tri_ctr = tri_ctr + len(common)
            cmp_l.append(j)
    print("\tTriangles: ",tri_ctr/6)
    return


class Node(object):
    def __init__(self):
        pass

    def betweenness(self):
        pass

    def degree_dist(self,G):  # This is Prob. 3-d.
        '''
        ----------------------
        parameter G: Graph
        ----------------------
        Find the degree of each node and return it.        
        '''
        deg = []
        for i in G.nodes:
            deg.append(G.degree(i))     
        return list(deg)

