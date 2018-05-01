import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
def compute_num_triangles(g):  # This is Prob. 3-e.
    '''
    Write your code documentation here.  # This is Prob. 4-a.
        Parameters
        ----------
        g: `graph`
            The graph is related about data.

        Returns
        -------
        total: total triangles
    '''

    tri = nx.triangles(g)
    total=sum(tri.values())/3
    return total


class Node(object):
    def __init__(self):
        pass

    def betweenness(self):
        pass

    def degree_dist(self,g):  # This is Prob. 3-d.
        '''
        Write your code documentation here.  # This is Prob. 4-a.
        Parameters
        ----------
        g: `graph`
            The graph is related about data.

        Returns
        -------
        g_degree: every id's degree
        '''
        g_degree=[]
        for i in range(len(g.degree())):
            g_degree.append(g.degree()[i])
        return g_degree

