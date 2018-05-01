import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

def changetoint(x):
    list1=[]
    for item in x:
        try:
            list1=list1+[int(item)]
        except:
            pass
    return list1
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

    def from_in_class_network(self,filename):  # This is Prob. 3-a.
        '''
        Read graph in edgelist txt format from `path`.

        Parameters
        ----------
        filename: `str`
            your target filename
        Returns
        -------
        G: `NetworkX graph`
           
        '''
        
        df=pd.read_csv(filename,sep="\t",index_col=0)
        self.g=nx.Graph(df["IDs-of-acquaintances"].str.split(",").apply(changetoint).to_dict())
        char=df.loc[:,["sex","age","department","time-to-bed"]].T.to_dict()
        nx.set_node_attributes(self.g,char)
        return self.g
