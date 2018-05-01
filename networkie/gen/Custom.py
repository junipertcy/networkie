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

    def from_in_class_network(self,r):  # This is Prob. 3-a.
        '''
        Write your code documentation here.  # This is Prob. 4-a.
         
         Parameters
        ----------
        r: file name
            use pandas to read a file 
            take two lines of information ['ID'] , ['IDs-of-acquaintances']
            for the value of ['IDs-of-acquaintances'] change from 'str' to 'int'
            add all number that exist in the value of ['ID'] and ['IDs-of-acquaintances']
       
        Returns
        ----------
        '''
        df = pd.read_csv('In-class-network.txt',delimiter = '\t')
        ID = df['ID']
        a = df['IDs-of-acquaintances']
        
        for i in range(len(a)):
            if "," in a[i]:
                a[i] = a[i].split(",")
                for j in range(len(a[i])):
                    a[i][j] = int(a[i][j])
            elif a[i] == ' ':
                continue
            else:
                a[i] = [int(a[i])]

            self.g.add_nodes_from(a[i])
            self.g.add_nodes_from(ID)

            for j in range(len(a[i])):
                self.g.add_edge(int(ID[i]),a[i][j])
        
        return self.g


