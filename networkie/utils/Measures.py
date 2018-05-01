import networkx as nx
import pandas as pd
def compute_num_triangles(gp):  # This is Prob. 3-e.
    '''
        compute the triangle

        Parameters
        ----------
        gp: a Undirected Graph
            a Graph you want to compute the triangular

        Returns
        -------
        number of triangular:int

    '''
    count=0
    adj=pd.Series(dict(gp.adj))
    for item in gp.edges():
        try:
    #         print(list(set(adj.loc[item[0]]).intersection(adj.loc[item[1]])))
            count=count+(len((list(set(adj.loc[item[0]]).intersection(adj.loc[item[1]])))))
    #         print(item,list(set(adj.loc[item[0]]).intersection(adj.loc[item[1]])))
        except:
    #         print(item)
            pass
#     gp.edges
    return count/3
class Node(object):
    def __init__(self):
        pass

    def betweenness(self):
        pass

    def degree_dist(self,gp):  # This is Prob. 3-d.
        '''
        Read graph in edgelist txt format from `path`.

        Parameters
        ----------
        path: `gp`
            a Graph you want to compute the triangular

        Returns
        -------
        list3: the list with Ki's degree

        '''
        list3=[]
        for items in (gp.degree):
            list3=list3+[items[1]]
        list3=list(pd.Series(list3).value_counts().sort_index())
        return list3

