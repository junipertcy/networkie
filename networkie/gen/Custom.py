import matplotlib.pyplot as plt
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

    def from_in_class_network(self):  # This is Prob. 3-a.
        #f = open('In-class_network.txt','r')
        data = pd.read_csv('In-class_network.txt', sep="\t")
        #print(data)
        #print(len(data.index))
        edgelist = []
        for i in range(0,len(data.index)):
            if data.iloc[i][1] != ' ':
                l =  list(map(int,(data.iloc[i][1].split(","))))
                #print(l)
                for j in range(data.iloc[i][1].count(",")+1):
                    edgelist += [[data.iloc[i][0],l[j]]]
                #print(data.iloc[i][0])
        #print(edgelist)
        self.g.add_edges_from(edgelist)
        print(nx.info(self.g))
        #print("Average path lenght: "+ nx.average_shortest_path_length(self.g))
        print("Average path length of subgraph: ")
        for C in nx.connected_component_subgraphs(self.g):
            print(nx.average_shortest_path_length(C))
        emax = ((self.g.number_of_nodes())*((self.g.number_of_nodes())-1))/2
        print("The e/emax: " , float(self.g.number_of_edges())/emax)
        ng = max(nx.connected_component_subgraphs(self.g), key=len)
        print("The size of the largest connected component:")
        nx.draw(ng, node_color = '#00BBFF', node_size = 200, with_labels = True)
        #nx.draw(self.g, node_color = '#00BBFF', node_size = 400, with_labels = True)
        #plt.show()
        return self.g

a = LoadFromFile()
a.from_in_class_network()