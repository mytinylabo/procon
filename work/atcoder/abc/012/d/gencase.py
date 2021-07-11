from random import randint
import networkx as nx

N = 400
M = 44850
W = (1, 1000)

G = nx.gnm_random_graph(N, M)

print(N, M)
for u, v in G.edges:
    print(u + 1, v + 1, randint(*W))
