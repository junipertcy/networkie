def compute_num_triangles(g):  # This is Prob. 3-e.
    '''
    Write your code documentation here.  # This is Prob. 4-a.
    
    Parameters
    ----------
    graph: `g`
        The graph that you want to compute the number of triangles.

    Returns
    -------
    int: `int`
        The number of triangles of a graph.
    '''
    triple_iter = ((n, nbr, nbr2) for n in g for nbr, nbr2 in combos(g[n],2) if nbr in g[nbr2])
    triangles = set(frozenset(tri) for tri in triple_iter)

    return len(triangles)


class Node(object):
    def __init__(self):
        pass

    def betweenness(self):
        pass

    def degree_dist(self):  # This is Prob. 3-d.
        '''
        Return a list that contains all nodes' degree. Note that if i is not in ID, its degree is 0.
        Also note that d, is the dictionary whose keys are ID and values are list of its adjacent nodes. 

        Parameters
        ----------
        None.

        Returns
        -------
        deg_list: `list`
            the list which contains all nodes' degree.

        '''
        global d
        deg_list=[0] * 75

            for k, v in d.items():
                if v != 999:
                    deg_list[k] = len(v)

        return deg_list

