import networkx as nx
def compute_num_triangles(g):  # This is Prob. 3-e.
    '''
    Read a NetworkX graph to count the total number of triangles.

    Parameters
    ----------
    g: `NetworkX graph`
        A parsed NetworkX graph.
    
    Returns
    -------
    triangle: `int`
        The total number of triangles(transitive triad) of the NetworkX graph.

    '''
    import pandas as pd
    import networkx as nx
    import numpy as np
    k = g.copy()
    count = 0
    pathlist = []
    component_size = []
    k.remove_nodes_from(list(nx.isolates(k)))
    connected_components = nx.connected_component_subgraphs(k)
    total_list = []
    for component in connected_components:
        if nx.number_of_nodes(component) >= 3:
            for items1 in component:
                for items2 in nx.all_neighbors(component,items1):
                    for items3 in nx.all_neighbors(component,items2):
                        if items1 in list(nx.all_neighbors(component,items3)):
                            three_list = []
                            three_list.append(int(items1))
                            three_list.append(int(items2))
                            three_list.append(int(items3))
                            three_list.sort()
                            total_list.append(three_list)
    total_list = np.array(total_list)    
    total_new_list = np.unique(total_list, axis=0)
    triangle = total_new_list.shape[0]
    return triangle
    


class Node(object):
    def __init__(self):
        import networkx as nx
        pass

    def betweenness(self):
        pass

    def degree_dist(self, g):  # This is Prob. 3-d.
        '''
        Read a NetworkX graph to establish a list of degree whose indexes correspond to the name of node.

        Parameters
        ----------
        g: `NetworkX graph`
            A parsed NetworkX graph.

        Returns
        -------
        final_list: `list`
            The list of degree of the NetworkX graph with indexes corresponding to the name of node.

        '''  
        import networkx as nx
        import numpy as np
        vertex_degree = []
        for index in g:
            index_int = int(index)
            vertex_degree.append([index_int,g.degree(index)])
        vertex_degree = np.array(vertex_degree)
        vertex_degree[vertex_degree[:, 0].argsort()]
        vertex_degree_sort = vertex_degree[vertex_degree[:, 0].argsort()]
        final_list = list(vertex_degree_sort[:,1])
        return final_list

