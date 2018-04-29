from Custom import *
from Measures import  *
import matplotlib.pyplot as plt
f=LoadFromFile()
print(type(f.from_in_class_network("In-class_network.txt")))
g=f.from_in_class_network("In-class_network.txt")
d=Node()
print(d.degree_dist(g))
print(compute_num_triangles(g))
