from random import randint
import networkx as nx
N = 50000
M = N * 3
W = (1, 20)

G = nx.gnm_random_graph(N, M, directed=True)

print(N, M, 0)
for u, v in G.edges:
    print(u, v, randint(*W))
