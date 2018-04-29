import pandas as pd

def compute_num_triangles():  # This is Prob. 3-e.
    '''
    Write your code documentation here.  # This is Prob. 4-a.
    '''

    return


class Node(object):
    def __init__(self):
        pass

    def betweenness(self):
        pass

    def degree_dist(self):  # This is Prob. 3-d.
        '''
        Write your code documentation here.  # This is Prob. 4-a.
        '''
        data = pd.read_csv('In-class_network.txt', sep="\t")
        #print(data)
        #print(len(data.index))
        edgelist = []
        for i in range(0,len(data.index)):
            if data.iloc[i][1] != ' ':
                #l =  list(map(int,(data.iloc[i][1].split(","))))
                #print(l)
                edgelist += [[data.iloc[i][0], data.iloc[i][1].count(",")+1]]
                #for j in range(data.iloc[i][1].count(",")+1):
                    #edgelist += [[data.iloc[i][0],l[j]]]
                    #print(data.iloc[i][0])
            else:
                edgelist += [[data.iloc[i][0], 0]]
        #print(edgelist)
        return edgelist

a = Node()
a.degree_dist()