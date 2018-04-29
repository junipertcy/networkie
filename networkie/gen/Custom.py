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

    def from_in_class_network(self,path):  # This is Prob. 3-a.
        '''
        Write your code documentation here.  # This is Prob. 4-a.

        Parameters
        ----------

        path: `str`
            The path to the edgelist text file. Note that the node index must start from 0.        
        
        Returns
        --------
        G: "NetworkX graph"
            The parsed graph.

        '''
        linelist=[]
        e=[]
        no=[]
        with open (path,"r") as F :
            for line in F :
                line=line.replace("\t",".").strip("\n").split(".")
                linelist.append(line)
        linelist=linelist[1:]
        for i in range(len(linelist)):
            linelist[i]=linelist[i][0:2]
            linelist[i][0]=int(linelist[i][0])
        for i in range(len(linelist)):
            if linelist[i][1].count(",")>=1:
                num=linelist[i][1].split(",")
                for d in num :
                    e+=[(linelist[i][0],int(d))]
            elif linelist[i][1]==" ":
                no+=[linelist[i][0]]
            else :
                e+=[(linelist[i][0],int(linelist[i][1]))]
        self.g.add_nodes_from(no)
        self.g.add_edges_from(e)
        return self.g
