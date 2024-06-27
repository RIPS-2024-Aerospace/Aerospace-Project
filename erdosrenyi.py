import networkx as nx
import matplotlib.pyplot as plt
import random

n = 10
P = 0.5
G = nx.Graph()
for i in range(n):
    for j in range(i, n):
        if random() >= P: 
            G.add_edge(i, j)

subax1 = plt.subplot(121)
nx.draw(G, pos=nx.circular_layout(G), node_color='r', edge_color='b')
