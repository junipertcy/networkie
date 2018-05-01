import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from Custom import LoadFromFile

g = nx.Graph ()
g = LoadFromFile.from_in_class_network ( g, "In-class_network.txt" )
# This is Prob. 3-e.
def compute_num_triangles():  
    Friend1, Friend2, count = [], [], 0
    for i in g.nodes:
        for j in range ( 0, len ( g.edges ( i ) ) ):
            Friend1.append ( list ( g.edges ( i ) ) [j][1] )
        for k in range ( 0, len ( Friend1 ) ):
            if len ( list ( g.edges ( Friend1[k] ) ) ) != 0:
                for l in range ( 0, len ( list ( g.edges ( Friend1[k] ) ) ) ):
                    Friend2.append ( list ( g.edges ( Friend1[k] ) )[l][1] )
        for m in range ( 0, len ( Friend2 ) ):
            if len ( list ( g.edges ( Friend2[m] ) ) ) != 0:
                for n in range ( 0, len ( list ( g.edges ( Friend2[m] ) ) ) ):
                    if i == list ( g.edges ( Friend2[m] ) )[n][1]:
                        count += 1
        Friend1, Friend2 = [], []

    # This is Prob. 4-a.
    '''
    從創造出的圖中找 Nodes
    → 再看這些 Nodes 的下一層，儲存在 Friend1
    → 從 Friend1 找這些 Nodes 的下一層，儲存在 Friend2
    → 再從 Friend2 找這些 Nodes 的下一層，如果裡面有最一開始的 Node 則 count 數加一
    → 由於組合問題，依照上述的方法，會將重複的集合重複計算，因此最後 return 的 count 應該除以 3! 才是實際的三角形數
    '''
    return ( count / 6 )
print ( "The total number of triangles in the network:  " + str ( compute_num_triangles() ) )

class Node(object):
    def __init__(self):
        pass

    def betweenness(self):
        pass

    # This is Prob. 3-d.
    def degree_dist(self):
        Degree = []
        for i in g.nodes:
            Degree.append ( g.degree (i) )
            Unique_Degree = list ( set ( Degree ) )
        Number = []
        for i in Unique_Degree:
            Number.append ( Degree.count ( i ) ) 
        
        # This is Prob. 4-a
        '''
        將每一個 Node 的 Degree 數存放在 [ Degree ] 裡面，把 Degree 不重複的存在 [ Unique_Degree ] 裡
        計算 Unique Degree 在 Degree 裡出現的次數存進 [ Number ] 裡
        再將 Degree、Number 對應畫出 bar chart        
        '''
        return Unique_Degree, Number

Unique_Degree, Number = Node.degree_dist ( g )
plt.title ( "Degree Distribution" ) # 打出圖表標題
plt.xlabel ( "Degree" ) # 打出 X 軸名稱
plt.ylabel ( "Number" ) # 打出 Y 軸名稱
plt.bar ( Unique_Degree , Number ) # 畫出 Degree 跟 Number
plt.show ()