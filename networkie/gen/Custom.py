import networkx as nx


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


    def from_in_class_network(self,path):  # This is Prob. 3-a.
        import pandas as pd   
        import numpy as np

        df = pd.read_table(path)
        IDstore =[]
        ID =[]
        data = np.array(list(zip(df['ID'], df['IDs-of-acquaintances']))) 

        for line in data:
            if line[1]==" " :          
                self.g.add_node(line[0])                    #若第二欄為0，則只將其編號放入g
            else:
                tempstore = line[1].split(',')              #其他，則將每一筆資料以區隔並存入
                for templine in tempstore:
                    self.g.add_edge(line[0],templine)
            tempstore.clear()

        print(nx.info(self.g))
        #print(self.g.nodes())
        print('Edgelist txt data successfully loaded into a networkx Graph!')    
        return self.g 



        
        