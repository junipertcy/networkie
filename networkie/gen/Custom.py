import networkx as nx
import pandas as pd

class LoadFromFile(object):
    def __init__(self):
        '''
        Initiate object a graph variable name 'g'
        '''
        self.g = nx.Graph()

    def from_edgelist(self, path):
        '''
        Read graph in edgelist txt format from `path`.

        Parameters
        ----------
        path: `str`
            The path to the edgelist text file. Note that the node index must start from 0.

        Returns
        -------
        G: `NetworkX graph`
            The parsed graph.
        '''

        edgelist = []
        with open(path, 'r') as f:
            for line in f:
                node_pair = line.replace('\n', '').split(' ')
                edgelist += [node_pair]
        self.g.add_edges_from(edgelist)
        print(nx.info(self.g))
        print('Edgelist txt data successfully loaded into a networkx Graph!')
        return self.g

    def from_in_class_network(self, filename='dataset/In-class_network.txt',
                              fillna='unknown', directed=False):
        '''
        read graph from csv file

        Parameters
        ----------
        filename : `str`, default 'In-class_network.txt', pathlib.Path
        fillna : `object`, default 'unknown', fill missing values of attributes
        directed : `bool`, default False, determine whether it's Graph or DiGraph

        Returns
        -------
        G: `networkx.DiGraph` object if directed is True
           else return `networkx.Graph`.
        '''
        Graph = nx.DiGraph if directed else nx.Graph
        # csv to Dataframe
        df = pd.read_csv(filename,
                         delimiter='\t' ,
                         index_col=0).iloc[:,:-1].fillna(fillna)
        # rename neighbors column
        df.rename(columns={ df.columns[0]:'neighbors'}, inplace=True)
        # turn neighbors to adjacency list
        adjacency = df.neighbors.apply(lambda x: eval('[%s]'%x)).to_dict()
        # create graph from adjacency list 
        self.g = Graph(adjacency)
        # other columns are attributes of nodes
        nx.set_node_attributes(self.g, df.drop('neighbors',1).T.to_dict() )

        return self.g
