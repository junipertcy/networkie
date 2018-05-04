def compute_num_triangles(G):  # This is Prob. 3-e.
    '''
    Analysis each node in the graph:
        First 'for' loop : Select the first node.
        Second 'for' loop : Store all the second nodes that the first node connected. 
        Third 'for' loop : Store all the third nodes that the second nodes connected.
        Forth 'for' loop : Store all the nodes that the third nodes connected.
        The last 'for' loop : Check if the third nodes connect to the first node.
                              If true -> tri_ctr + 1
    After finish all the steps : 
		Return the value: tri_ctr/6 -> because each traingle would be counted 6 times. 
    '''
    tri_ctr = 0
    for i in G.nodes:
        first_node_tmp = [e for e in G.edges(i)]
        first_node = (first_node_tmp[0][0])      #逐點進行分析
        num = len(first_node_tmp)
        
        second_node = []                         #存下連接到的第二點
        for j in range(num):
            second_node.append(first_node_tmp[j][1])
            second_node_tmp = [e for e in G.edges(second_node[j])]
            
            third_node = []                      #存下連接到的第三點
            for k in range(len(second_node_tmp)):
                third_node.append(second_node_tmp[k][1])
                third_node_tmp = [e for e in G.edges(third_node[k])]
             
                third_node_connect = []          #判斷第三點是否能連回第一點(形成三角形)
                for l in range(len(third_node_tmp)):
                    third_node_connect.append(third_node_tmp[l][1])
                
                for m in range(len(third_node_connect)):
                    if first_node == third_node_connect[m]:
                        tri_ctr = tri_ctr + 1

    print("The total number of triangles:",tri_ctr/6) 
    
    return


class Node(object):
    def __init__(self):
        pass

    def betweenness(self):
        pass

    def degree_dist(self,G):  # This is Prob. 3-d.
        '''
        Count the degree of each node in the graph.
        Store the values in a list and return it. 
        '''
        degree = []
        for i in G.nodes:
            degree.append(G.degree(i)) 
        
        return list(degree)

