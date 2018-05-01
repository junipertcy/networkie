def compute_num_triangles(g):  # This is Prob. 3-e.
    import networkx as nx
    import numpy as np

    triangles = nx.triangles(g)
    total=sum(triangles.values())/3  
    return total
    '''
    Write your code documentation here.  # This is Prob. 4-a.
    利用nx.triangles 來計算三角形個數，因為每個點都會重複計算，
    所以要將算出的值除以三
    '''


class Node(object):
    def __init__(self):
        pass

    def betweenness(self):
        pass

    def degree_dist(self,g):  # This is Prob. 3-d.
        import numpy as np
        import networkx as nx
        degree_store = dict(g.degree)
        # print(degree_store) 
        # print(list(degree_store.values()))    
        dimension =list(degree_store.values()) 
        '''
        Write your code documentation here.  # This is Prob. 4-a.
        引入numpy，networkx ，利用g.degree找出各個維度，並將每一維度的值存成一個list
        '''
        return dimension

