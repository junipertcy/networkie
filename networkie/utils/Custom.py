import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class LoadFromFile ( object ):
    def __init__ ( self ):
        self.g = nx.Graph ()
        return self.g

    # This is Prob. 3-a.        
    def from_in_class_network ( self, Filename ):
        ID, Friends = [], []
        for line in open ( Filename ):
            if 'ID' in line:
                continue
            Line = line.strip ()
            ID.append ( int ( Line.split ( "\t" ) [0] ) )
            Friends.append ( eval ( "[" + Line.split ( "\t" ) [1] + "]" ) ) # 用 eval 把字串內的東西存起來
            
        Data = dict ( zip ( ID, Friends ) )
        self.g = nx.Graph ( Data )
        # nx.draw ( self.g, node_size = 10 )
        # plt.show ()
        return self.g

    # This is Prob. 4-a.
        '''
        在 __init__ 先初創一個空的 Graph
        在 from_in_class_network 創造兩個串列
        ID 存放 "In-class_network.txt" 裡第一列的數字
        Friends 存放 "In-class_network.txt" 裡第二列的數字
        建立 ID 跟 Friends 的連結以 Dictionary 的形式存放，再用 nx.Graph 畫出圖形
        '''

g = nx.Graph ()
g = LoadFromFile.from_in_class_network ( g, "In-class_network.txt" )
nx.draw ( g, node_size = 10 )
plt.show ()

###############################################################################################################

# This is Prob. 3-b
print ( nx.info ( g ) )
# (i) The number of nodes = 75
# (ii) The number of edges = 109
# (iii) Average degree = 2.9067

print ( "Average path length:   " + str ( int ( g.order() ) / int ( g.size() ) ) ) # 用 Node 個數除以 Edge 個數得 Average path length 
# (iv) Average path length = 0.6880733944954128

nG = max ( nx.connected_component_subgraphs ( g ), key = len )
print ( "Size of the largest connected component:   " + str ( nG.size() ) )
# (v) The size of the largest connected component = 70

###############################################################################################################

# This is Prob. 3-c
Fully_Connected_Network = g.copy() # 複製一個跟 g 一樣的圖
for i in Fully_Connected_Network.nodes: # 用 i 取出 Fully_Connected_Network 中的每一個 Nodes
    for j in Fully_Connected_Network.nodes: # 同樣用 j 取出 Fully_Connected_Network 中的每一個 Nodes
        if i != j: # 當 i 跟 j 不相等時，幫他們兩個加上 Edges
            Fully_Connected_Network.add_edge ( i, j )
e_max = len ( Fully_Connected_Network.edges ) # 算 Fully_Connected_Network 的 Edges 個數
e = len ( g.edges ) # 算 g 中的 Edges 個數
print ( "e / e_max: " + str ( e / e_max ) )