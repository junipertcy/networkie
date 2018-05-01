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

    def from_in_class_network(self, path='./dataset/In-class_network.txt', print_info='True'):  # This is Prob. 3-a.
        '''
        # This is Prob. 4-a.
        
        Read graph from the file "In-class_network.txt".
        
        Parameters
        ----------
        path: `str`
            The path of the file "In-class_network.txt", default './dataset/In-class_network.txt'.
        print_info: `bool`
            The boolean flag which allow to show the common descriptive statistics or not, default True.
        
        Returns
        -------
        G: `NetworkX graph`
            The parsed graph.
        
        '''
        self.g=nx.Graph()
        with open(path, 'r') as f:
            next(f)
            for line in f:
                node_pairs = line.replace('\n', '').split('\t')
                adj_nodes = node_pairs[1].replace(' ', '').split(',')
                self.g.add_node(int(node_pairs[0]), sex=node_pairs[2], age=int(node_pairs[3]), department=node_pairs[4], time_to_bed=node_pairs[5])
                if '' in adj_nodes:
                    pass
                else:
                    for adj_node in adj_nodes:
                        self.g.add_edge(int(node_pairs[0]),int(adj_node))
        #print(nx.info(self.g))
        print('Descriptive statistics of the graph:')
        print('------------------------------------')
        print('Number of nodes (n): ', nx.number_of_nodes(self.g))
        print('------------------------------------')
        print('Number of edges (e): ', nx.number_of_edges(self.g))
        print('------------------------------------')
        print('Average degree (k): ', round(sum(d for n, d in nx.degree(self.g))/len(self.g), 4))
        print('------------------------------------')
        print('There are %d connected components in the graph, and the average shortest path (l) for each connected components are:' %len(list(nx.connected_component_subgraphs(self.g))))
        for component in nx.connected_component_subgraphs(self.g):
            print('  ', round(nx.average_shortest_path_length(component), 4))
        print('------------------------------------')
        print('The size of the largest connected component (n_G): ', len(max(nx.connected_component_subgraphs(self.g), key=len)))
        print('------------------------------------')
        fc_g = nx.complete_graph(nx.number_of_nodes(self.g))
        print('If the network is fully connected, the max number of edges (e_max) will be: ', nx.number_of_edges(fc_g))
        print('The edges of the original network divided by the max number of edges (e/e_max) will be: ', round( nx.number_of_edges(self.g)/nx.number_of_edges(fc_g), 4))
        return self.g
