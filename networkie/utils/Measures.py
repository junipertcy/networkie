import networkx as nx
def compute_num_triangles(graph):  # This is Prob. 3-e.
    n_tri=0
    for a in list(graph.nodes()):
        nei=list(graph.neighbors(a))
        for j in range(len(nei)):
            l=list(range(len(nei)))[j+1:]
            for k in l:
                if nx.has_path(graph,nei[j],nei[k]):
                    if list(nx.shortest_path(graph,source=nei[j],target=nei[k]))==[nei[j],nei[k]]:
                       n_tri+=1
    n_tri=n_tri/3

    '''
    take the two nodes from neighbor nodes in permutation,
    then check the route of these two whether the route length is equal to 2
    '''
    return n_tri


class Node():
    def __init__(self,graph):
        self.graph=graph

    def degree_dist(self):  # This is Prob. 3-d.
        vectors=[]
        for a in sorted(self.graph.nodes()):
            nei=len(list(self.graph.neighbors(a)))
            vectors.append(nei)

        '''
        find the degree by  the id's acquaintance
        '''
        return vectors

