'''
    Test if the function Node.degree_dist in networkie/utils/Measures work properly.
'''

from networkie.gen.Custom import LoadFromFile
from networkie.utils.Measures import Node


class TestDegree:
    def test_degree_and_edge(self):
        G = LoadFromFile().from_in_class_network('dataset/In-class_network.txt')
        sum_of_degrees = sum(Node(G).degree_dist())
        assert sum_of_degrees/2 == G.size()