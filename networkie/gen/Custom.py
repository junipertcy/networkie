import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

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

    def from_in_class_network(self,path='In-class_network.txt'):  # This is Prob. 3-a.
        '''
        Write your code documentation here.  # This is Prob. 4-a.

        read graph from the class_network text file.

        Parameters
        ----------
        path: `str`
            The path to the class_network text file. 

        Returns
        -------
        G: `NetworkX graph`
            The parsed graph.

        '''

        df = pd.read_csv(path,delimiter="\t") # using pandas's DataFrame to store the info of graph.
        df.drop(df.columns[6],axis=1,inplace=True) # drop the last column coming from nowhere.
        df['IDs-of-acquaintances'][df['IDs-of-acquaintances'] == ' '] = '999' # set the absent value in 'IDs-of-acquaintances' to be '999'.

        '''-----------making dict for nodes & edges-----------'''
        d = df.set_index('ID')['IDs-of-acquaintances'].to_dict() # combine 'ID' and 'IDs-of-acquaintances' and form a dict.
        d = {k: v.split(',') for k, v in d.items()} # change the value from string to list.
        d = {k: [int(i) for i in v] for k, v in d.items()} # change the value from string to integer.

        self.g.add_nodes_from(d.keys()) # adding nodes for graph g.
        for k, v in d.items():
            if v != 999: # discard the absent value in 'IDs-of-acquaintances'.
                self.g.add_edges_from(([(k, t) for t in v])) # adding edges for graph g.
        return self.g
