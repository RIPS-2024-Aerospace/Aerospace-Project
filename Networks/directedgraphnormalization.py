import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import random

# Param G: directed, weighted graph
# Returns G with normalized adj matrix
def normalize(G):
    mx = nx.adjacency_matrix(G)
    rowsum = np.array(mx.sum(1))
    r_inv = np.power(rowsum, -1).flatten()
    r_inv[np.isinf(r_inv)] = 0.
    r_mat_inv = sp.sparse.diags(r_inv)
    mx = r_mat_inv.dot(mx)
    return nx.Graph(mx)




