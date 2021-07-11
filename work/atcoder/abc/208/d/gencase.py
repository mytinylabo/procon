from random import randint
import networkx as nx

N = 200
M = N * (N - 1)
W = (1, 10**6)

G = nx.gnm_random_graph(N, M)

print(N, len(G.edges))
for u, v in G.edges:
    print(u + 1, v + 1, randint(*W))
