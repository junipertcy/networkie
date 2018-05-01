import sys
sys.path.append("./networkie/")
from utils import Measures

class TestComputeDegrees:
    def test_degree_dist(self):
        import network as nx
        import numpy as np
        
        degree_list = [[1, 1], [2, 3], [4, 6], [5, 3], [6, 3], [7, 5], [8, 2], [9, 8], [12, 5], [13, 4], [15, 4], [18, 4], [19, 4], [20, 3], [23, 1], [24, 3], [25, 3], [26, 0], [28, 1], [29, 1], [30, 2], [31, 3], [33, 5], [35, 3], [36, 1], [37, 3], [39, 1], [41, 4], [43, 2], [44, 1], [45, 2], [47, 3], [48, 3], [49, 5], [50, 1], [51, 2], [52, 1], [53, 3], [54, 1], [55, 1], [56, 2], [57, 0], [58, 1], [60, 1], [62, 1], [64, 2], [65, 1], [66, 0], [67, 2], [68, 1], [69, 4], [70, 6], [71, 1], [72, 0], [73, 3], [74, 0]]  
        degree_list = np.array(degree_list)
        g = nx.Graph()
        g.add_edges_from(data_list)
        n = nx.number_of_nodes(g)
        e = nx.number_of_edges(g)
        degrees = (2 * e/n)
        
        degree_list = Measures.Node()
        g_degree = degree_list.degree_dist(g)
        g_degree = np.array(g_degree)
        x = np.average(g_degree)     
        expected = degrees
        result = x
        
        assert expected == result