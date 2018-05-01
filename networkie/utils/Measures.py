def compute_num_triangles(G):  # This is Prob. 3-e.
    '''
    Write your code documentation here.  # This is Prob. 4-a.

    用 edgelist 存成每個 node 對應到的 neighbor ，利用這個字典去找三個互相連接的 node ，並存到 tri 中
    若三個一組的 node 已經在 tri 中，就不存進去，最後回傳 len(tri) ，也就是有幾個 triangles
    '''
    node = list(G.nodes())
    edgelist = {}
    tri = []
    for i in node:
        if len(G.edges(i)) != 0:
	        cur = []
	        for j in list(G.edges(i)):
	            cur.append(j[1])
	        edgelist[i] = cur

    for i in list(edgelist.keys()):
	    for j in edgelist[i]:
	        for k in edgelist[j]:
	            if i in edgelist[k] and sorted([i, j, k]) not in tri:
	                tri.append(sorted([i, j, k]))
    return len(tri)


class Node(object):
    def __init__(self):
        pass

    def betweenness(self):
        pass

    def degree_dist(self):  # This is Prob. 3-d.
        '''
        Write your code documentation here.  # This is Prob. 4-a.

        node 用來存圖中有幾個 node ，用一個迴圈從 ID = 1 的 node 呼叫 degree ，並存在 degree_dist 中，最後回傳 degree_dist。

        '''
        degree_dist = []
        node = list(self.nodes())

        for i in range(len(node)):
        	degree_dist.append(self.degree(str(i)))

        return degree_dist

