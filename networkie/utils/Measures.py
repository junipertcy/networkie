def compute_num_triangles(G):  # This is Prob. 3-e.
    '''
    Calculates the total number of triangles in the network

    Parameters
    ----------
    G: `NetworkX graph`

    Returns
    -------
    num_of_triangle: `int`
    	number of triangle in a network
    '''
    def nodes_connected(u, v):
    	return u in G.neighbors(v)
    t= 0
    for i in  G.nodes():
    	neighbors = list(G.neighbors(i))
    	pairs = [(i,v) for i in neighbors for v in neighbors if i!=v]
    	for u,s in pairs:
    		if nodes_connected(u,s):t+=1
    num_of_triangle = t/6
    return num_of_triangle


class Node(object):
    def __init__(self):
        pass

    def betweenness(self):
        pass

    def degree_dist(self,G):  # This is Prob. 3-d.
        '''
        Caculate the degree distibution of each node in a Graph

        Parameters
        ----------
        G: `NetworkX graph`

        Returns
        -------
        vector_k: `list`
        	elements are the degrees ki of vertex i
        '''
        vector_k = list(dict(G.degree).values())
        return vector_k

