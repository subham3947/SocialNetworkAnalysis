import numpy as np
import networkx as nx
import time
import matplotlib.pyplot as plt
start_time = time.clock()
n=943
m=429128
p=float((2*m))/float((n*(n-1)))
print p
G=nx.erdos_renyi_graph(n, p)
print nx.average_shortest_path_length(G)
print nx.average_clustering(G)
#print nx.average_shortest_path_length(G)
#degree_sequence=sorted(nx.degree(G).values(),reverse=True)
#dmax=max(degree_sequence)
#plt.loglog(degree_sequence,'b-',marker='o')
#plt.show()
#nx.draw(G)
#plt.show(G)
#plt.savefig("ER_RG_Epinions.png")

