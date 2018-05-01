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
        Write your code documentation here.  # This is Prob. 4-a.
        
        Parameters
        ----------
        path: `str`
            The path to the edgelist text file.
        
        Returns
        -------
        G: `NetworkX graph`
            The parsed graph.
        
        '''
        df = pd.read_table(path)
        n = []
        for i in range(df["ID"].shape[0]):
            n.append(df["ID"][i])
        L = []
        for i in list(df["IDs-of-acquaintances"]):
            i = i.split(",")
            L.append(i)
        for i in range(len(L)):
            for j in range(len(L[i])):
                if L[i][j] != " ":
                    L[i][j] = int(L[i][j])
        for i in range(len(L)):
            for j in range(len(L[i])):
                if L[i][j] != " " and L[i][j] not in n:
                    n.append(L[i][j])
        self.g.add_nodes_from(n)
        e = []
        for i in range(len(L)):
            if ' ' not in L[i]:
                for j in range(len(L[i])):
                    e.append((df["ID"][i], L[i][j]))
        self.g.add_edges_from(e)
                
        return self.g
