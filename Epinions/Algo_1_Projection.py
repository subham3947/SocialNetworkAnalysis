import numpy as np
import networkx as nx
#import community
import NetProp
#import time
import UserDistribution
#import matplotlib.pyplot as plt
#start_time = time.clock()
f = open('Biadjacency.txt')
triplets=f.read().split()
for i in range(0,len(triplets)): triplets[i]=triplets[i].split(',')
B=np.array(triplets, dtype=np.uint8)
Biadjacency=B.reshape(65,4667)
np.savetxt('Graph_Adj.txt', Biadjacency, fmt='%d')
Adjacency=np.zeros(shape=(65,65))
for i in range(1,66):
     print(i)
     for j in range(1,66):
         for k in range(1,4668):
             if Biadjacency[i-1][k-1] == 1 and   Biadjacency[i-1][k-1]==  Biadjacency[j-1][k-1] and i!=j:
                Adjacency[i-1][j-1]=1
#print (np.sum(Adjacency))
#print(Adjacency)
n=len(Adjacency[0])
e=np.sum(Adjacency)/2
G=nx.from_numpy_matrix(Adjacency)
NetProp.clusterCoeff(G)
NetProp.GiantComponent(G)
NetProp.density(n,e)
NetProp.erdos(n,e)
UserDistribution.Dist(Adjacency)
G=UserDistribution.erdos(n,e)
A=nx.to_numpy_matrix(G)
A = np.squeeze(np.asarray(A))
print('Erdos')
UserDistribution.Dist(A)
#Gc1 = max(nx.connected_component_subgraphs(G), key=len)
#Gc=list(sorted(nx.connected_components(G), key = len, reverse=True))
#print('No. of nodes in the giant components of the graph',len(Gc[0]))
#print('Average shortest path length',nx.average_shortest_path_length(Gc1))
#print(Gc)
#nx.draw(Gc)
#plt.savefig("path.png")
#degree_sequence=sorted(nx.degree(G).values(),reverse=True)
#dmax=max(degree_sequence)
#plt.loglog(degree_sequence,'b-',marker='o')
#plt.show()
#print nx.average_clustering(G)
#print nx.average_shortest_path_length(G)
#print time.clock() - start_time
