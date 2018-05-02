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

    def from_in_class_network(self, path):  # This is Prob. 3-a.
        df = pd.read_csv(path, delimiter = "\t",index_col = 0 )
        edges = []
        self.g = nx.Graph()
        for node , value in  df.iterrows():
            int_num_list = []
            sum_str = value["IDs-of-acquaintances"].strip().split(",")
            for i in sum_str:
                if i:
                    int_num_list.append(int(i))
            new_list = []
            for i in id_list:
                for j in int_num_list:
                    new_list.append((i,j))
            tmp = [(node, v) for v in int_num_list]
            self.g.add_edges_from(tmp)

        '''
        Write your code documentation here.  # This is Prob. 4-a.
        '''
        return self.g
c= 