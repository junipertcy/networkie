import networkx as nx
import pandas as pd
import csv
import numpy as np 
import matplotlib.pyplot as plt
#-*-coding:utf-8-*-




class LoadFromFile(object):
    
    def __init__(self):
        """
        Initiate variables for the class.
        Loading the data from file. 
        """
        path = "dataset/In-class_network.txt"
        self.data = open(path,"r")
        
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

    def from_in_class_network(self):  
        '''
        Reading the desinated file and build the graph.
        Choosing Col. ID and Col. IDs-of-acquaintances as nodes ,building the undirected edge as the relationship. 
        '''
        first_read = True                                       #Skip the header column name of data.
        for row in self.data:
            x= row.split("\t")
            if first_read == False: 
                for i in x[1].split(","):
                    if i != " " and x[0] != " ":
                        e = [(x[0],i)]                          #define the edge from "ID" to "IDs-of-acquaintances"
                        self.g.add_edges_from(e)
            first_read = False
        return self.g 



