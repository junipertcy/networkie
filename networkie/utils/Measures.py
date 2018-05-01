def compute_num_triangles(g):  # This is Prob. 3-e.
    '''
    Read a networkx graph to count the total of triangles in it.
    
    Parameters
    ----------
    g: `NetworkX graph`
       The graph created from networkx. 
    
    Returns
    -------
    n/3: `int`
        The total triangles(transitive triad) of the NetworkX graph.
    
    '''
    import networkx as nx
    import itertools
    n = 0
    for e in e_iter(g):
        if g.has_edge(e[1][0], e[1][1]) or g.has_edge(e[1][1], e[1][0]):
            n += 1
    return n/3
    
def e_iter(g):
    for node in g.nodes_iter():
        neighbors = g.neighbors(node)
        for pair in itertools.combinations(neighbors, 2):
            yield (node, pair)
        
class Node(object):
    def __init__(self):
        pass

    def betweenness(self):
        pass

    def degree_dist(self,g):  # This is Prob. 3-d.
        '''
        Read a networkx graph to count the degrees of every node in it.
        
        Parameters
        ----------
        g: `NetworkX graph`
            The graph created from networkx. 

        Returns
        -------
        degree_list: `Python list`
            The list is the degree of the nodes in NetworkX graph.
        
        '''
        
        import networkx as nx
        import numpy as np
        degree_list = []
        for i in g:
            degree_list.append(g.degree(i))
        #print(degree_list)
        return degree_list
        '''
        data = pd.read_csv('In-class_network.txt', sep="\t")
        #print(data)
        #print(len(data.index))
        edgelist = []
        for i in range(0,len(data.index)):
            if data.iloc[i][1] != ' ':
                #l =  list(map(int,(data.iloc[i][1].split(","))))
                #print(l)
                edgelist += [[data.iloc[i][0], data.iloc[i][1].count(",")+1]]
                #for j in range(data.iloc[i][1].count(",")+1):
                    #edgelist += [[data.iloc[i][0],l[j]]]
                    #print(data.iloc[i][0])
            else:
                edgelist += [[data.iloc[i][0], 0]]
        print(edgelist)
        return edgelist
        '''
        
'''
g=nx.complete_graph(3)
a = Node()
print(a.degree_dist(g))

print('Number of triangles:', compute_num_triangles(g))

'''
