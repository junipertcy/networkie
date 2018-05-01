'''
    Test if the *.edgelist data in dataset/bipartite is really bipartite.
    Warning: it only applies to edgelist data that has its node index ordered
'''

from os import listdir
from os.path import isfile, join

basepath = 'dataset/bipartite/'

files = [f for f in listdir(basepath) if isfile(join(basepath, f))]
edgelist_files = [f for f in files if f[-9:] == '.edgelist']


def test_bipartiteness():
    type_a_set = set()
    type_b_set = set()

    for filepath in edgelist_files:
        with open(basepath + filepath, 'r') as f:
            delimiter = ''  # this line is not necessary for Python
            for idx, line in enumerate(f):
                if idx == 0:  # decide the correct delimiter for the data
                    node_pair = ['']
                    possible_delimiters = [' ', ',', '\t']
                    while len(node_pair) == 1:
                        delimiter = possible_delimiters.pop()
                        node_pair = line.replace('\n', '').split(delimiter)
                node_pair = line.replace('\n', '').split(delimiter)

                type_a_node = node_pair[0]
                type_b_node = node_pair[1]
                type_a_set.add(type_a_node)
                type_b_set.add(type_b_node)
    if len(type_a_set.intersection(type_b_set)) == 0:
        _assert = True
    else:
        _assert = False

    assert _assert
