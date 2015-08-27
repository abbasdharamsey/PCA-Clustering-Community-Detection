import numpy
import scipy
import math
import networkx as nx
from collections import defaultdict

print ""

egonet = open('egonet.txt', 'r')

edges = set()
nodes = set()
for edge in egonet:
    x,y = edge.split()
    x,y = int(x),int(y)
    edges.add((x,y))
    edges.add((y,x))
    nodes.add(x)
    nodes.add(y)

G = nx.Graph()
for e in edges:
    G.add_edge(e[0], e[1])

num_of_nodes = nx.number_of_nodes(G)
num_of_edges = nx.number_of_edges(G)

print "Question 1"
print "----------\n"
print "Number of nodes:", num_of_nodes
print "Number of edges:", num_of_edges, "\n"

num_of_conn_components = nx.number_connected_components(G)
largest_conn_component = list(nx.connected_component_subgraphs(G))[0]
num_of_nodes_in_largest_conn_component = nx.number_of_nodes(largest_conn_component)

print "Question 2"
print "----------\n"
print "Number of connected components:", num_of_conn_components
print "Number of nodes in largest component:", num_of_nodes_in_largest_conn_component, "\n"

communities = list(nx.k_clique_communities(G, 4))
num_of_communities = len(communities)

community_list = []
for fset in communities:
    community_list.append(list(fset))

print "Question 3"
print "----------\n"
print "Number of communities:", num_of_communities
print "Communities:"
for i, comm in enumerate(community_list):
    print "   " + str(i+1) + ":", comm
