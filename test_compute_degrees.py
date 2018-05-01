from networkie.gen import Custom
from networkie.utils import Measures
lff = Custom.LoadFromFile()
g = lff.from_in_class_network('dataset/In-class_network.txt')
Node= Measures.Node()
l=Node.degree_dist(g)

class Testdegree:
    def test_degree(self):
        expected=g.size()
        result=sum(Node.degree_dist(g))/2
        
        assert expected==result
   




