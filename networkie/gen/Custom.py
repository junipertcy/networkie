import networkx as nx
import matplotlib.pyplot as plt

class LoadFromFile(object):
    def __init__(self):
        """
        Initiate variables for the class.
        """
        self.g = nx.Graph()


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
        return self.g

    def from_in_class_network(self,path):  # This is Prob. 3-a.edge
        # This is Prob. 4-a.
        '''
        Read graph in edgelist txt format from 'path'.

        Parameters
        ----------
        path:'str'
            The path is indicated the existed file.

        Returns
        -------
        G: 'NetworkX graph'
            The graph generated from the file.
        '''
        edgelist=[]
        with open(path,'r') as file:
            title=list(file.readline().split(' '))
            line=file.readline()
            while len(line)>0:
                #read each line to create the nodes and edges
                line=list(line.strip('\n').split('\t'))
                target=list(line[1].split(','))
                for i in range(len(target)):
                    if target[i]==' ':
                        self.g.add_node(int(line[0]))
                        continue
                    edgelist.extend([(int(line[0]),int(target[i]))])
                    #append the inverse edges
                    if (int(target[i]),int(line[0])) not in edgelist:
                        edgelist.extend([(int(target[i]),int(line[0]))])
                line=file.readline()
            self.g.add_edges_from(edgelist)
        return self.g

    def Avg_degree(self,G):
        '''
        Compute the average degree of the graph 'G'.

        Parameters
        ----------
        G:'graph'
            The existed graph we wnat to know.

        Returns
        -------
        avg_degree: 'float'
            The average degree of the graph.
        '''
        temp=list(G.degree())
        sum_degree=0
        #compute the sum of degree of each node's degree
        for i in range(len(temp)):
            sum_degree+=temp[i][1]
        avg_degree=sum_degree/len(temp)
        return avg_degree
