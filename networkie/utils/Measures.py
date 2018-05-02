import numpy as np
import pandas as pd

def compute_num_triangles(g):  # This is Prob. 3-e.
    '''
        Write  a function to calculate total numbers of triangles.

        Parameters
        ----------
        g : `NetworkX graph`
            The parsed graph.

        Returns
        -------
        count : `int`
            The total numbers
        '''

    tri = pd.DataFrame(data=np.array(g.edges()))
    for i in range(len(tri)):
        if tri.iloc[i, 0] > tri.iloc[i, 1]:
            tri.iloc[i, 0], tri.iloc[i, 1] = tri.iloc[i, 1], tri.iloc[i, 0]
    tri = pd.DataFrame(data=tri.sort_values(by=[0]))
    count = 0
    for i in range(len(tri)):
        for ii in range(i + 1, len(tri)):
            if tri.iloc[ii, 0] == tri.iloc[i, 0]:
                for iii in range(ii + 1, len(tri)):
                    if tri.iloc[i, 1] > tri.iloc[ii, 1]:
                        if (tri.iloc[iii, 0] == tri.iloc[ii, 1]) & (tri.iloc[iii, 1] == tri.iloc[i, 1]):
                            count = count + 1
                    else:
                        if (tri.iloc[iii, 0] == tri.iloc[i, 1]) & (tri.iloc[iii, 1] == tri.iloc[ii, 1]):
                            count = count + 1
    return count


class Node(object):
    def __init__(self):
        pass

    def betweenness(self):
        pass

    def degree_dist(self,g):  # This is Prob. 3-d.
        '''
            Write a function to output the list of degrees.

            Parameters
            ----------
            g : `NetworkX graph`
                The parsed graph.

            Returns
            -------
            vk: `list`
                The list of degrees
            '''

        vk = []
        for i in range(len(g.degree)):
            vk.append(g.degree[i])
        return vk
