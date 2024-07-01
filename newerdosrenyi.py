import networkx as nx
import matplotlib.pyplot as plt
import random
from math import comb

G = nx.Graph()
n = 10
c = 3 #avg degree
e = (c*n)/2 #total edges
P = e/comb(n, 2) #density

for i in range(n):
    for j in range(i+1, n):
        if random.random() <= P: 
            G.add_edge(i, j)

subax1 = plt.subplot(121)
nx.draw(G, pos=nx.circular_layout(G), node_color='r', edge_color='b')