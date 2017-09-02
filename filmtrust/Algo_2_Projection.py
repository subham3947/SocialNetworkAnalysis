import numpy as np
import networkx as nx
#import community
import ItemDistribution
import NetProp
import matplotlib.pyplot as plt
#start_time = time.clock()
f = open('Biadjacency.txt')
triplets=f.read().split()
for i in range(0,len(triplets)): triplets[i]=triplets[i].split(',')
B=np.array(triplets, dtype=np.uint8)
Biadjacency=B.reshape(1508,2071)
np.savetxt('Graph_Adj.txt', Biadjacency, fmt='%d')
Adjacency=np.zeros(shape=(2071,2071))
Biadjacency=Biadjacency.transpose()
for i in range(1,2072):
     print(i)
     for j in range(1,2072):
         for k in range(1,1509):
             if Biadjacency[i-1][k-1] == 1 and   Biadjacency[i-1][k-1]==  Biadjacency[j-1][k-1] and i!=j:
                Adjacency[i-1][j-1]=1
#print Adjacency
#print np.sum(Adjacency)
#print ('No. of Edges=')
#print (np.sum(Adjacency))/2
n=len(Adjacency[0])
e=np.sum(Adjacency)/2
G=nx.from_numpy_matrix(Adjacency)
NetProp.clusterCoeff(G)
NetProp.GiantComponent(G)
NetProp.density(n,e)
NetProp.erdos(n,e)
ItemDistribution.Dist(Adjacency)
G=ItemDistribution.erdos(n,e)
A=nx.to_numpy_matrix(G)
A = np.squeeze(np.asarray(A))
print('Erdos')
ItemDistribution.Dist(A)