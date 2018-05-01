import networkx as nx

def compute_num_triangles(g):  # This is Prob. 3-e.
    '''
    # This is Prob. 4-a.
    
    Compute the traingles in the network (using len() can get the number of the triangles).
    
    Parameters
    ----------
    g: `NetworkX graph`
        The Networkx graph which will be compute the triangles.

    Returns
    -------
    tri_list: `list`
        The list whose elements are the triangle tuples (using len(tri_list) can get the number of the triangles)
    
    '''
    tri_list=[]
    for node_i in g.nodes():
        for node_i_j in sorted(g.edges(node_i)):
            node_j=(node_i_j)[1]
            if node_j < node_i:
                continue
            for node_j_h in sorted(g.edges(node_j)):
                node_h=(node_j_h)[1]
                if node_h < node_j:
                    continue
                if node_i in g[node_h]:
                    tri_list.append((node_i,node_j,node_h))
    return tri_list


class Node(object):
    def __init__(self):
        pass

    def betweenness(self):
        pass

    def degree_dist(self,g):  # This is Prob. 3-d.
        '''
        # This is Prob. 4-a.
        
        Calculate the degrees of each nodes in the graph `g`.
        
        Parameters
        ----------
        g: `NetworkX graph`
            The Networkx graph which will be calculated the degrees.

        Returns
        -------
        nodes_degree: `list`
            The list whose elements are the degrees of each nodes.
        
        '''
        nodes_degree=[]
        for i in range(len(g.degree)):
            nodes_degree.append(g.degree[i])
        return nodes_degree

