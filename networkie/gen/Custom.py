import networkx as nx


class LoadFromFile():
    def  __init__(self,filename):

        self.filename=filename
    def from_in_class_network(self):  # This is Prob. 3-a.
        f=open(self.filename,'r')
        d=[]
        for i in f.readlines() :
            li=i[:len(i)-1].split('\t')
            d.append(li)

        G=nx.Graph()
        for i in d:
           G.add_node(int(i[0]), sex=i[2],age=int(i[3]),dep=i[4],sleep=i[5]) 

        for i in d:
            if i[1]==' ':
                continue
            friend=i[1].split(',')
            for j in friend:
                G.add_edge(int(i[0]), int(j))
        '''
        first , turn txt file into list
        second , put id number into Graph as nodes
        third, put the acquaintance data into Graph as edge
        '''
        return G
print(LoadFromFile('In-class network.txt').from_in_class_network().nodes())