import networkx as nx
from networkie.utils import Measures


def test_compute_degrees():

    filepath = 'dataset/karate.edgelist'

    g = nx.Graph()
    edgelist = []

    with open(filepath, 'r') as f:
        for line in f:
            node_pair = line.replace('\n', '').split(' ')
            edgelist += [(int(node_pair[0]),int(node_pair[1]))]
    g.add_edges_from(edgelist)
    nodes=Measures.Node()
    nodes_degrees=nodes.degree_dist(g)
    
    if sum(nodes_degrees) == sum(d for n, d in nx.degree(g)):
        _assert = True
    else:
        _assert = False

    assert _assert