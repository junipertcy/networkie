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

    def from_in_class_network(self, in_class_network):  # This is Prob. 3-a.
        '''
        Write your code documentation here.  # This is Prob. 4-a.
        這個function將接受結構和in-class_network相同的資料，先將讀進來的檔案，用'\t'切割後存在data中，
        取 ID 去和 IDs-of-acquaintances 中的每一個node配對後存在edgelist中，最後用 add_edges_from 存，
        如果 IDs-of-acquaintances 是空字串，就用add_node 存 ID。

        '''
        data = []
        edgelist = []

        with open(in_class_network, 'r') as f:
            for line in f:
                cur = line.replace('\n', '').split('\t')
                data += [cur]
        for i in range(len(data)):
            data[i][1] = data[i][1].split(',')

        for i in range(1, len(data)):
            if data[i][1] != [' ']:
                for j in range(len(data[i][1])):
                    edgelist += [[data[i][0], data[i][1][j]]]
            else:
                self.g.add_node(data[i][0])

        self.g.add_edges_from(edgelist)
        return self.g
