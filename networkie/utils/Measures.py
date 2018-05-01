def compute_num_triangles(g):  # This is Prob. 3-e.
    '''
    Write your code documentation here.  # This is Prob. 4-a.
    
    Parameters
    ----------
    count how many triangles for each node and sum all triangles ,because it count repeatly therefore then divid by 3

    Returns
    -------
    g: `NetworkX graph`
    '''
    t = nx.triangles(g)
    return print('number of triangles :',sum(t.values())/3)

    return


class Node(object):
    def __init__(self):
        pass

    def betweenness(self):
        pass

    def degree_dist(self):  # This is Prob. 3-d.
        '''
        Write your code documentation here.  # This is Prob. 4-a.

        Parameters
        ----------
        put every degree into list
    
        '''
        degree = []
        for i in range((G.order())):
            degree.append(G.degree(i))
            
        return degree()

