#!/usr/bin/python3

import matplotlib.pyplot as plt
import networkx as nx
import sys

nodes = []
edges = []

for line in sys.stdin:
    edgefrom,edgeto = line.strip().split(": ")
    edgesto = edgeto.split(" ")
    nodes.append(edgefrom)
    for i in edgesto:
      nodes.append(i)
      edges.append((edgefrom, i))

nodes = list(dict.fromkeys(nodes))

G = nx.Graph()
G.add_nodes_from(nodes)
for i in edges:
  G.add_edge(*i)
# uncomment to draw graph
#nx.draw(G, with_labels=True, node_color='yellow')
#plt.savefig("graph.png")
print(len(nx.node_connected_component(G, "qqq")))
print(len(nx.node_connected_component(G, "mlp")))
