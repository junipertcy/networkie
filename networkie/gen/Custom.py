import networkx as nx
import pandas as pd
import numpy as np

class LoadFromFile(object):
    def __init__(self):
        """
        Initiate variables for the class.
        """
        self.g = nx.Graph()

        pass

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

    def from_in_class_network(self,data_r):  # This is Prob. 3-a.
        '''
        Write  a function to turn the data of  txt file to a  networkx graph.

        Parameters
        ----------
        data_r: `str`
            The file name and path of  'In-class_network.txt'.

        Returns
        -------
        g : `NetworkX graph`
            The parsed graph.
        '''
        stats = pd.read_table(data_r)
        stats.iloc[:, 1] = stats.iloc[:, 1].str.split(',')
        self.g.add_nodes_from(stats['ID'].values)
        edge = []
        for i in range(len(stats)):
            for j in range(len(stats.iloc[i, 1])):
                if stats.iloc[i, 1][j] != " ":
                    edge.append([stats.iloc[i, 0], int(stats.iloc[i, 1][j])])
        self.g.add_edges_from(edge)
        return self.g
