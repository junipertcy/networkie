from Custom import LoadFromFile
import networkx as nx
def compute_num_triangles(G):  # This is Prob. 3-e.
    '''
    # This is Prob. 4-a.
    Compute the number of the triangles from the graph.

    Parameters
    ----------
    G: 'NetwokX graph'
        Graph is from the file constructing the nodes.

    Returns
    -------
    len(friends): 'int'
                   The number of the triangles. 
    '''
    peo={}
    for i in range(len(G)):
        peo[i]=list(G.neighbors(i))
    friends=[]
    for i in range(len(peo)):
        for k in range(len(peo[i])):
            friend=peo[i][k] #common friend
            for j in range(len(peo[friend])):
                if peo[friend][j] in peo[i]:
                    common=sorted([i,friend,peo[friend][j]]) #avoid same pair
                    if common not in friends:
                        friends.extend([common])
    return len(friends)

def recommend_friend(G): 
    '''
    To build a potential friends list to each node.

    Parameters
    ----------
    G: 'NetwokX graph'
        The resource graph we want to construct the potential list.

    Returns
    -------
    recommend_friend: 'dict'
                   The list which key is the node and the content is the list 
                    of its potential friends. 
    '''
    nodes=list(G.nodes())
    recommend_friend={}
    #create the list type storing the potential friends
    for i in range(len(nodes)):
        recommend_friend[i]=[]

    for num in range(len(nodes)):
        #nodes[num] is the mutual friend
        check=list(G.neighbors(nodes[num]))
        #check is the list of the nodes[num]'s friends
        for i in range(len(check)):
            peoples=list(G.neighbors(check[i]))
            #peoples is the detected person's friends
            for k in range(len(check)):
                #check[k] is the person also in mutual friend's friends
                if i==k:
                    continue
                if check[k] not in peoples and check[k] not in recommend_friend[check[i]]: #check[i] does not know check[k]
                    recommend_friend[check[i]].append(check[k])

    return recommend_friend

def mutual_friends(G,domain_firends,re_friends): #domain_firends(list),re_friends(dict)
    '''
    To find the best three potential friends of NO.45

    Parameter
    ---------
    G: 'NetworkX graph'
        The social network.

    domain_firends: 'list'
                    The list of NO.45's friends.

    re_friends: 'dict'
                The dictionary contains NO.45's potential friends.

    Returns
    -------
    friend: 'list'
            The best 3 potential friends we want to recommend to NO.45.
    '''
    potential=re_friends[45]
    friend=[]
    for rank in range(3):
        max_num,max_fri=0,-1
        for i in range(len(potential)): #potential friend
            temp=0
            for j in range(len(domain_firends)): #In NO.45's friends
                #comapre the potential person's friends and NO.45's friends' friends
                domain_list=list(G.neighbors(domain_firends[j]))
                for a in range(len(domain_list)):
                    if domain_list[a] in G.neighbors(potential[i]):
                        temp+=1
            if temp>max_num and potential[i] not in friend:
                max_num=temp
                max_fri=potential[i]
        friend.append(max_fri)
    return friend

class Node(object):
    def __init__(self):
        pass

    def betweenness(self):
        pass

    def degree_dist(self, G):  # This is Prob. 3-d.
        '''
        # This is Prob. 4-a.
        Compute the distribution of the degree.

        Parameter
        ---------
        G: 'NetworkX graph'
            The graph is created from the file.

        Returns
        -------
        degree: 'list'
                The list of all nodes' degree.
        '''
        # there are some lack ID #
        degree=[]
        nodes=list(G.nodes())
        for i in range(len(nodes)):
            #degree conrains in and out degree
            n=G.degree(nodes[i])
            degree.append(n)
        return degree
