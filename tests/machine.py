import networkx as nx

def degree_dist(self): 

    degree_dist = []
    node = list(self.nodes())

    for i in range(len(node)):
    	degree_dist.append(self.degree(str(i)))

    return degree_dist