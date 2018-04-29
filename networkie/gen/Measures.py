import pandas as pd
import networkx as nx
def compute_num_triangles(g):  # This is Prob. 3-e.
    '''
    Write your code documentation here.  # This is Prob. 4-a.

    Parameter
    ----------

    g : `NetworkX graph`
            The parsed graph.

    Returns
    -------
    tri : integral
        Calculates the total number of triangles in the network
    '''
    tri=[]
    for i in nx.connected_components(g):
        if len(i)>=3:
            for j in i :
                num=()
                for d in g.edges(j): 
                    for z in g.edges(d[1]):
                        if z[1]!=j:  
                            for c in g.edges(z[1]): 
                                if c[1]==j:
                                    num=tuple(sorted([d[0],d[1],z[1]]))
                                    tri+=[num]
    tri=len(set(tri))
    return tri


class Node(object):
    def __init__(self):
        pass

    def betweenness(self):
        pass

    def degree_dist(self,g):  # This is Prob. 3-d.
        '''
        Write your code documentation here.  # This is Prob. 4-a.
        
        Parameter
        -----------
        g : `NetworkX graph`
            The parsed graph.
        
        Returns
        ----------
        vector_k : "list"
            vector_k is a list whose elements are the degrees k of the "ID" from the text>

        
        '''
        vector,degree=[],[]
        for i in g.nodes():
            vector+=[i]
            degree+=[len(g.edges(i))]
        ki=pd.DataFrame({"vector":vector,"degree":degree})
        ki=ki.sort_values(by="vector")
        vector_k=[]
        ki2=ki["degree"].value_counts().sort_index()
        for i in ki.index:
            vector_k+=[(ki.loc[i]["vector"],ki2[ki.loc[i]["degree"]])]
        return vector_k
