import numpy as np
import networkx as nx
import ItemDistribution
import NetProp
#start_time = time.clock()
f = open('Biadjacency.txt')
triplets=f.read().split()
for i in range(0,len(triplets)): triplets[i]=triplets[i].split(',')
B=np.array(triplets, dtype=np.uint8)
Biadjacency=B.reshape(943,1682)
#print Biadjacency
Biadjacency=Biadjacency.transpose()
Adjacency=np.zeros(shape=(1682,1682))
#print Adjacency
for i in range(1,1683):
     print(i)
     for j in range(1,1683):
        for k in range(1,944):
            if Biadjacency[i-1][k-1] == 1 and   Biadjacency[i-1][k-1]==  Biadjacency[j-1][k-1] and i!=j:
               Adjacency[i-1][j-1]=1
n=len(Adjacency[0])
e=np.sum(Adjacency)/2
#print('No. of Edges=',e)
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