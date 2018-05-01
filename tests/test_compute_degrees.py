'''
    Test if the function degree_dist in Measures.py work
'''

import sys
sys.path.append("./networkie/")
from utils import Measures
    
class TestComputeDegrees:
    def test_degree_dist(self):
        import networkx as nx
        '''
        expected = g.number_of_edges()
        result = sum(degree_dist(g))/2
        '''
        g = nx.complete_graph(3)
        a = Measures.Node()
        a.degree_dist(g)
        expected = g.number_of_edges()
        result = sum(a.degree_dist(g))/2
        assert expected == result