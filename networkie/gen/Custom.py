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

    def from_in_class_network(self,s):  # This is Prob. 3-a.
    
        '''
        Write your code documentation here.  # This is Prob. 4-a.
        Parameters
        ----------
        s:open file 
            open and read file
            Grab two lines information['IDs-of-acquaintances']["ID"]
            Change data from string to int
            combine ID and acquaintances
        Returns
        -------
        g: `NetworkX graph`
        '''
        df=pd.read_csv(s,delimiter = '\t')
       
        id_1=df["ID"]
        a=df['IDs-of-acquaintances']

        for i in range(len(a)):
            if "," in a[i]:        
                a[i] = a[i].split(",")
                for j in range(len(a[i])):
                    a[i][j]=int(a[i][j])
                    
            elif a[i]==" ":
                continue
                
            else:
                a[i] =[int(a[i])]

            self.g.add_nodes_from(a[i])
            self.g.add_nodes_from(id_1)
            for j in range(len(a[i])):
                self.g.add_edge(int(id_1[i]),a[i][j])
        return self.g
