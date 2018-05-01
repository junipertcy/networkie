def compute_num_triangles(g):  # This is Prob. 3-e.
    '''
    Write your code documentation here.  # This is Prob. 4-a.

    Parameters
    ----------
    compute how many triangles does each node has and sum of it ,then devide 3 

    Returns
    -------
    g: `NetworkX graph`
    '''
    tri = nx.triangles(g)   
    return print("number of triangles:",sum(tri.values())/3)

    return


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
        put degrees into list
        draw a graph

        Returns
        -------
        g: `NetworkX graph`
        '''
        l=[]
        for i in range(len(g.nodes())):
            l.append(g.degree(i))
            
        return l


