import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
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

    def from_in_class_network(self,path):  # This is Prob. 3-a.
        '''
        Write your code documentation here.  # This is Prob. 4-a.
        
        Parameters
        ----------
        path: `file`
            The path is about what data you want to know.
        Returns
        -------
        G: `NetworkX graph`
            The parsed graph.
        '''
        one = []
        with open(path,"r") as f:
            for line in f:
                line = line.strip().split("\t")
                one.append(line)
        one=pd.DataFrame(one[1:],columns=one[0])
        
        ID=[]
        ID_node=[]
        for i in range(len(one)):
            if one["IDs-of-acquaintances"][i]==" ":
                ID_node.append(int(one["ID"][i]))
            if one["IDs-of-acquaintances"][i]!=" ":    
                ID.append(one["ID"][i])
                ID.append(one["IDs-of-acquaintances"][i])

        for i in range(1,len(ID),2):
            ID[i]=ID[i].split(",")

        number=[]
        for j in range(1,len(ID),2):
            for k in range(len(ID[j])):
                number.append((int(ID[j-1]),int(ID[j][k])))

        self.g=nx.Graph()
        self.g.add_nodes_from(ID_node)
        self.g.add_edges_from(number)
        return self.g 
