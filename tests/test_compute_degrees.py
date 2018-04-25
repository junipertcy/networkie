'''
    Test if the test_degree_dist function really works well.
'''
import sys
sys.path.append("./networkie/")
from utils import Measures

class TestComputeDegrees:
    def test_degree_dist(self):
        import networkx as nx
        import numpy as np
        data_list = [[1, 0],[2, 0],[2, 1],[3, 0],[3, 1],[3, 2],[4, 0],[5, 0],[6, 0],[6, 4],[6, 5],[7, 0],[7, 1],[7, 2],[7, 3],[8, 0],[8, 2],[9, 2],[10, 0],[10, 4],[10, 5],[11, 0],[12, 0],[12, 3],[13, 0],[13, 1],[13, 2],[13, 3],[16, 5],[16, 6],[17, 0],[17, 1],[19, 0],[19, 1],[21, 0],[21, 1],[25, 23],[25, 24],[27, 2],[27, 23],[27, 24],[28, 2],[29, 23],[29, 26],[30, 1],[30, 8],[31, 0],[31, 24],[31, 25],[31, 28],[32, 2],[32, 8],[32, 14],[32, 15],[32, 18],[32, 20],[32, 22],[32, 23],[32, 29],[32, 30],[32, 31],[33, 8],[33, 9],[33, 13],[33, 14],[33, 15],[33, 18],[33, 19],[33, 20],[33, 22],[33, 23],[33, 26],[33, 27],[33, 28],[33, 29],[33, 30],[33, 31],[33, 32]]
        data_list = np.array(data_list)
        g = nx.Graph()
        g.add_edges_from(data_list)
        n = nx.number_of_nodes(g)
        e = nx.number_of_edges(g)
        degrees = (float(2.0) * e/n)
        degree_list = Measures.Node()
        g_degree = degree_list.degree_dist(g)
        g_degree = np.array(g_degree)
        x = np.average(g_degree)     
        expected = degrees
        result = x
        
        assert expected == result