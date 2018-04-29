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

    def from_in_class_network(self, path):  # This is Prob. 3-a.
        '''
        Read graph in In-class_network txt format from `path`.

        Parameters
        ----------
        path: `str`
            The path to the In-class_network text file. Note that the node index must start from 0.

        Returns
        -------
        G: `NetworkX graph`
            The parsed graph.

        '''
        import numpy as np
        In_class_network = []
        In_class_network_for_use = []
        with open(path, 'r') as f:
            for line in f:
                everyline = line.replace('\t', 'abc').split('abc')
                everyline = np.array(everyline)
                In_class_network += [everyline]
        del In_class_network[0]
        In_class_network_new = np.array(In_class_network, dtype = object)
        In_class_network_for_use = In_class_network_new[:, 0:2]
        In_class_network_for_use[In_class_network_for_use == " "] = "0" 
        for line in In_class_network_for_use:
            if line[1] == "0":
                self.g.add_node(line[0])
            else:
                temp_list = line[1].split(',')
                for templine in temp_list:
                    self.g.add_edge(line[0],templine)
            temp_list.clear()
        print(nx.info(self.g))
        print('Edgelist txt data successfully loaded into a networkx Graph!')
        return self.g
