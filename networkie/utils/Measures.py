def compute_num_triangles(G):
    '''
    see function `triangles`
    '''
    return len(list(triangles(G)))

def triangles(G):
    '''
    find all triangle of a graph by BFS, 
    triangle located between n and n+1 level of BFS tree, 
    check tie between nodes at same level, found thier neighbor in common
    
    Parameter
    ---------
    G : networkx graph object, could be either directed or not,
        this function turn G to undirected and find triangle.
    
    Yeilds
    ------
    generator types
    yeild tuples. ex: (3, 4, 5) where 3, 4, 5 are name of nodes
    '''
    friends_of = { node: set(neb) for node, neb in G.adj.items()}
    traveled = set()
    # for a graph, find triangles from each connected component
    while len(traveled) < len(friends_of):
        root = (set(G.node)- traveled).pop()
        traveled.add(root)
        lvl_n = {root}
        # for each component, do bfs search
        while lvl_n:
            next_lvl, poped = set(), set()
            # for each level of bfs, find triangles between lvl_n, nodes on same level
            while lvl_n:
                someone = lvl_n.pop()
                poped.add(someone)
                smones_frnd = friends_of[someone]
                next_lvl |= smones_frnd-traveled
                counted_tri = set()
                # for lvl_n knew each other
                for other in smones_frnd & lvl_n:
                    # find their friends in common and exclude triangles already counted 
                    for friend in (friends_of[other] & smones_frnd) \
                                            - (poped|counted_tri):
                        yield (friend, someone, other)
                    counted_tri.add(other)
            traveled |= next_lvl
            lvl_n = next_lvl

class Node(object):
    def __init__(self, G):
        self.degree = list(G.degree)
        
    def betweenness(self):
        pass

    def degree_dist(self):
        '''
        list of degree 
        '''
        assert all( list(map(lambda tup: isinstance(tup[0], int) , self.degree)))
        return [deg for ID, deg in sorted(self.degree, key=lambda x:x[0]) ]


