import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

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

    def from_in_class_network(self):  #parses the 'In-class network.txt' file to a networkx Graph object  #3a

        df = pd.read_csv(self,sep = '\t').iloc[0:,:-5]  
        
        idd = df['ID']
        ids = df['IDs-of-acquaintances'] #take column 'ID' & column 'IDs-of-acquaintances'

        idss = []
        for i in range(len(ids)):
            idss.append(ids[i].split(",")) 

        #[['58'], ['56', '34', '25'], ['13', '18', '66', '61', '5', '10'], ['66', '13', '18'], 
        #['19', '53', '38'], ['3', '21', '17', '69', '63'], ['70', '20'], ['40', '51', '39', '32', '46', '27', '71', '24'], 
        #['65', '39', '9', '24', '22'], ['4', '66', '18', '61'], ['27', '35', '67', '70'], ['66', '13', '4', '42'], 
        #['38', '6', '53', '64'], ['35', '68', '70'], ['28'], ['71', '39', '51'], ['2', '56', '57'], [' '], ['23'],
        #['68'], ['2', '56'], ['48', '43', '37'], ['17', '69', '63', '7', '3'], ['67', '70', '20'], ['6'], ['52', '43', '48'],
        #['51'], ['64', '38', '71', '24'], ['48', '37'], ['59'], ['25', '2'], ['11', '56', '25'], ['43', '31', '37'],
        #['73', '72', '64', '11', '47'], ['55'], ['39', '46'], ['37'], ['19', '6', '38'], ['10'], ['50'], ['2', '30'], 
        #[' '], ['68'], ['62'], ['16'], ['73', '49'], ['14'], [' '], ['35', '6'], ['58'], ['63', '17', '3', '7'], 
        #['35', '20', '38', '67', '0', '44'], ['24'], [' '], ['49', '72', '64'], [' ']]

        idsss = []
        for i in range(len(idss)):
            for j in range(len(idss[i])):
                idsss.append(idss[i][j])

        #['58', '56', '34', '25', '13', '18', '66', '61', '5', '10', '66', '13', '18', '19', '53', '38', '3', '21', '17', '69',
        #'63', '70', '20', '40', '51', '39', '32', '46', '27', '71', '24', '65', '39', '9', '24', '22', '4', '66', '18', '61', 
        #'27', '35', '67', '70', '66', '13', '4', '42', '38', '6', '53', '64', '35', '68', '70', '28', '71', '39', '51', '2', '56', 
        #'57', ' ', '23', '68', '2', '56', '48', '43', '37', '17', '69', '63', '7', '3', '67', '70', '20', '6', '52', '43', '48',
        #'51', '64', '38', '71', '24', '48', '37', '59', '25', '2', '11', '56', '25', '43', '31', '37', '73', '72', '64', '11',
        #'47', '55', '39', '46', '37', '19', '6', '38', '10', '50', '2', '30', ' ', '68', '62', '16', '73', '49', '14', ' ',
        #'35', '6', '58', '63', '17', '3', '7', '35', '20', '38', '67', '0', '44', '24', ' ', '49', '72', '64', ' ']


        nw = []
        for i in range(len(idsss)):
            if idsss[i] == ' ':
                 nw.append(100)
            else:
                 nw.append(int(idsss[i]))

        #[58, 56, 34, 25, 13, 18, 66, 61, 5, 10, 66, 13, 18, 19, 53, 38, 3, 21, 17, 69, 63, 70, 20, 40, 51, 39, 
        #32, 46, 27, 71, 24, 65, 39, 9, 24, 22, 4, 66, 18, 61, 27, 35, 67, 70, 66, 13, 4, 42, 38, 6, 53, 64, 35,
        #68, 70, 28, 71, 39, 51, 2, 56, 57, 100, 23, 68, 2, 56, 48, 43, 37, 17, 69, 63, 7, 3, 67, 70, 20, 6, 52, 
        #43, 48, 51, 64, 38, 71, 24, 48, 37, 59, 25, 2, 11, 56, 25, 43, 31, 37, 73, 72, 64, 11, 47, 55, 39, 46, 37, 
        #19, 6, 38, 10, 50, 2, 30, 100, 68, 62, 16, 73, 49, 14, 100, 35, 6, 58, 63, 17, 3, 7, 35, 20, 38, 67, 0, 44, 
        #24, 100, 49, 72, 64, 100]


        edge = []
        for i in range(len(idd)):
            for j in range(len(ids[i].split(","))):
                edge.append([idd[i],ids.values[i].split(",")[j]])

        #[[1, '58'], [2, '56'], [2, '34'], [2, '25'], [4, '13'], [4, '18'], [4, '66'], [4, '61'], [4, '5'], [4, '10'], 
        #[5, '66'], [5, '13'], [5, '18'], [6, '19'], [6, '53'], [6, '38'], [7, '3'], [7, '21'], [7, '17'], [7, '69'], 
        #[7, '63'], [8, '70'], [8, '20'], [9, '40'], [9, '51'], [9, '39'], [9, '32'], [9, '46'], [9, '27'], [9, '71'], 
        #[9, '24'], [12, '65'], [12, '39'], [12, '9'], [12, '24'], [12, '22'], [13, '4'], [13, '66'], [13, '18'], [13, '61'], 
        #[15, '27'], [15, '35'], [15, '67'], [15, '70'], [18, '66'], [18, '13'], [18, '4'], [18, '42'], [19, '38'], [19, '6'], 
        #[19, '53'], [19, '64'], [20, '35'], [20, '68'], [20, '70'], [23, '28'], [24, '71'], [24, '39'], [24, '51'], [25, '2'], 
        #[25, '56'], [25, '57'], [26, ' '], [28, '23'], [29, '68'], [30, '2'], [30, '56'], [31, '48'], [31, '43'], [31, '37'], 
        #[33, '17'], [33, '69'], [33, '63'], [33, '7'], [33, '3'], [35, '67'], [35, '70'], [35, '20'], [36, '6'], [37, '52'], 
        #[37, '43'], [37, '48'], [39, '51'], [41, '64'], [41, '38'], [41, '71'], [41, '24'], [43, '48'], [43, '37'], [44, '59'], 
        #[45, '25'], [45, '2'], [47, '11'], [47, '56'], [47, '25'], [48, '43'], [48, '31'], [48, '37'], [49, '73'], [49, '72'], 
        #[49, '64'], [49, '11'], [49, '47'], [50, '55'], [51, '39'], [51, '46'], [52, '37'], [53, '19'], [53, '6'], [53, '38'], 
        #[54, '10'], [55, '50'], [56, '2'], [56, '30'], [57, ' '], [58, '68'], [60, '62'], [62, '16'], [64, '73'], [64, '49'], 
        #[65, '14'], [66, ' '], [67, '35'], [67, '6'], [68, '58'], [69, '63'], [69, '17'], [69, '3'], [69, '7'], [70, '35'], 
        #[70, '20'], [70, '38'], [70, '67'], [70, '0'], [70, '44'], [71, '24'], [72, ' '], [73, '49'], [73, '72'], [73, '64'], 
        #[74, ' ']]

        iddd = []
        for i in range(len(edge)):
            iddd.append(edge[i][0])

        #[1, 2, 2, 2, 4, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 12, 12, 12, 12, 12, 13, 
        #13, 13, 13, 15, 15, 15, 15, 18, 18, 18, 18, 19, 19, 19, 19, 20, 20, 20, 23, 24, 24, 24, 25, 25, 25, 26, 28, 29, 30, 30, 
        #31, 31, 31, 33, 33, 33, 33, 33, 35, 35, 35, 36, 37, 37, 37, 39, 41, 41, 41, 41, 43, 43, 44, 45, 45, 47, 47, 47, 48, 48, 
        #48, 49, 49, 49, 49, 49, 50, 51, 51, 52, 53, 53, 53, 54, 55, 56, 56, 57, 58, 60, 62, 64, 64, 65, 66, 67, 67, 68, 69, 69, 
        #69, 69, 70, 70, 70, 70, 70, 70, 71, 72, 73, 73, 73, 74]

        edge1 = []
        for i in range(len(iddd)):
            edge1.append((iddd[i],nw[i])) # produce a list of edges
        
        #[(1, 58), (2, 56), (2, 34), (2, 25), (4, 13), (4, 18), (4, 66), (4, 61), (4, 5), (4, 10), (5, 66), (5, 13), (5, 18), 
        #(6, 19), (6, 53), (6, 38), (7, 3), (7, 21), (7, 17), (7, 69), (7, 63), (8, 70), (8, 20), (9, 40), (9, 51), (9, 39), 
        #(9, 32), (9, 46), (9, 27), (9, 71), (9, 24), (12, 65), (12, 39), (12, 9), (12, 24), (12, 22), (13, 4), (13, 66), 
        #(13, 18), (13, 61), (15, 27), (15, 35), (15, 67), (15, 70), (18, 66), (18, 13), (18, 4), (18, 42), (19, 38), (19, 6), 
        #(19, 53), (19, 64), (20, 35), (20, 68), (20, 70), (23, 28), (24, 71), (24, 39), (24, 51), (25, 2), (25, 56), (25, 57), 
        #(26, 100), (28, 23), (29, 68), (30, 2), (30, 56), (31, 48), (31, 43), (31, 37), (33, 17), (33, 69), (33, 63), (33, 7), 
        #(33, 3), (35, 67), (35, 70), (35, 20), (36, 6), (37, 52), (37, 43), (37, 48), (39, 51), (41, 64), (41, 38), (41, 71), 
        #(41, 24), (43, 48), (43, 37), (44, 59), (45, 25), (45, 2), (47, 11), (47, 56), (47, 25), (48, 43), (48, 31), (48, 37), 
        #(49, 73), (49, 72), (49, 64), (49, 11), (49, 47), (50, 55), (51, 39), (51, 46), (52, 37), (53, 19), (53, 6), (53, 38), 
        #(54, 10), (55, 50), (56, 2), (56, 30), (57, 100), (58, 68), (60, 62), (62, 16), (64, 73), (64, 49), (65, 14), (66, 100), 
        #(67, 35), (67, 6), (68, 58), (69, 63), (69, 17), (69, 3), (69, 7), (70, 35), (70, 20), (70, 38), (70, 67), (70, 0), 


        G = nx.Graph()

        G.add_edges_from(edge1) # add a list of edges
        G.to_undirected() #change graph to undirected
        G.remove_node(100) #remove node
        
        nx.draw(G, node_color = '#00BBFF', node_size = 25) # define a function to draw the graph
        plt.show() #show the graph
 
LoadFromFile.from_in_class_network('C:\Python35\workspace\In-Class_network.txt')