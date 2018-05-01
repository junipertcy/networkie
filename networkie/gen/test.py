import networkx as nx
import matplotlib.pyplot as plt

Filename = "In-class_network.txt"
graph = nx.Graph()
ID,Friends = [], []
for line in open ( Filename ):
	if 'ID' in line:
		continue
	Line = line.strip()
	ID.append ( int ( Line.split("\t") [0] ) )
	Friends.append ( eval ( "[" + Line.split("\t") [1] + "]" ) )
	# Friends.append ( eval ( "[" + Line.split("\t") [1] + "]" )  )

Data = dict ( zip ( ID, Friends ) )
print ( Data )

graph = nx.Graph( Data )
nx.draw ( graph )
plt.show()

Friend1, Friend2, count = [], [], 0
for i in graph.nodes:
	for j in range ( 0, len ( graph.edges ( i ) ) ):
		Friend1.append ( list ( graph.edges ( i ) ) [j][1] )
	for k in range ( 0, len ( Friend1 ) ):
		if len ( list ( graph.edges ( Friend1[k] ) ) ) != 0:
			for l in range ( 0, len ( list ( graph.edges ( Friend1[k] ) ) ) ):
				Friend2.append ( list ( graph.edges ( Friend1[k] ) )[l][1] )
	for m in range ( 0, len ( Friend2 ) ):
		if len ( list ( graph.edges ( Friend2[m] ) ) ) != 0:
			for n in range ( 0, len ( list ( graph.edges ( Friend2[m] ) ) ) ):
				if i == list ( graph.edges ( Friend2[m] ) )[n][1]:
					count += 1
	Friend1, Friend2 = [], []
print ( count / 6 )