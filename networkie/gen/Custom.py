import networkx as nx
import pandas as pd


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
        Parameters
        ----------
        path: `str`
            The path to the In-class_network text file.

        Returns
        -------
        G: `NetworkX graph`

        '''
        Write your code documentation here.  # This is Prob. 4-a.
        df=pd.read_table(path)
        G=nx.Graph()
        List=[]
        for i in range(df.shape[0]):
    		a=df["IDs-of-acquaintances"][i]
    		if a=="":
                G.add_node(df["IDs-of-acquaintances"][i])
    			continue
    		a=a.split(",")
    		for j in range(len(a)):
        		List=List+[(df["ID"][i],int(a[j]))]
        G.add_edges_from(List)
        return self.g
