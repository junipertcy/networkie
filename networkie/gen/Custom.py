import networkx as nx


class LoadFromFile(object):
    def __init__(self):
        '''
        Initiate variables for the class.
        '''
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

    def from_in_class_network(self,data):  # This is Prob. 3-a.
        '''
        Read the in-class data from txt file .

        Parameters
        ----------
        data: `str`
            The path and txt file name of th inclass data 

        Returns
        -------
        G: `NetworkX graph`
        '''
        df = pd.read_table(data)
        G = nx.Graph()
        for node , friends in df[["ID","IDs-of-acquaintances"]].values:
        	if " " in friends:
        		G.add_node(node)
        		continue
        	friends - list(map(int,friends.split(",")))
        	G.add_edges_from(list(zip([node]*len(friends),friends)))
        return self.g
