def compute_num_triangles(G):  # This is Prob. 3-e.
    '''
    Write your code documentation here.  # This is Prob. 4-a.
    '''
    def nodes_connected(u, v):
    	return u in G.neighbors(v)
    t= 0
    for i in  G.nodes():
    	neighbors = list(G.neighbors(i))
    	pairs = [(i,v) for i in neighbors for v in neighbors if i!=v]
    	for u,s in pairs:
    		if nodes_connected(u,s):t+=1
    return t/6


class Node(object):
    def __init__(self):
        pass

    def betweenness(self):
        pass

    def degree_dist(self):  # This is Prob. 3-d.
        '''
        Write your code documentation here.  # This is Prob. 4-a.
        '''
        return list()

