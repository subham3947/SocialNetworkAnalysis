import numpy as np
import networkx as nx
import UserDistribution
import time
import NetProp
import matplotlib.pyplot as plt
start_time = time.clock()
f = open('Biadjacency.txt')
triplets=f.read().split()
for i in range(0,len(triplets)): triplets[i]=triplets[i].split(',')
B=np.array(triplets, dtype=np.uint8)
Biadjacency=B.reshape(943,1682)
#print Biadjacency
Adjacency=np.zeros(shape=(943,943))
#print Adjacency
for i in range(1,944):
     print(i)
     for j in range(1,944):
         for k in range(1,1683):
             if Biadjacency[i-1][k-1] == 1 and  Biadjacency[i-1][k-1]==  Biadjacency[j-1][k-1] and i!=j:
                Adjacency[i-1][j-1]=1
n=len(Adjacency[0])
e=np.sum(Adjacency)/2
#print('No. of Edges=',e)
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
'''
count=0
Degree=[0]*943
for i in range(1,944):
     for j in range(1,944):
          if (Adjacency[i-1][j-1]==1):
               count=count+1
     Degree[i-1]=count
     count=0
print Degree
print max(Degree)
CountDegree=[0]*max(Degree)
probability=[0]*max(Degree)
for j in range(1, max(Degree)+1):
    for i in range(0, len(Degree)):
       if j==Degree[i]:
            CountDegree[j-1]=CountDegree[j-1]+1
print CountDegree
for j in range(1, max(Degree)+1):
     probability[j-1]=float(CountDegree[j-1])/943
print probability
Maxdegree=[0]*max(Degree)
for i in range(1, max(Degree)+1):
    Maxdegree[i-1]=i
print Maxdegree
plt.loglog( Maxdegree,probability,'r^')
plt.xlabel ('Degree Value')
plt.ylabel('probability (Pk)')
plt.show()
#print Adjacency
#print np.sum(Adjacency)
#print ('No. of Edges=')
#print (np.sum(Adjacency))/2
#G=nx.from_numpy_matrix(Adjacency)
##Gc = max(nx.connected_component_subgraphs(G), key=len)
##print nx.average_shortest_path_length(Gc)
##nx.draw(Gc)
#plt.savefig("path.png")
#degree_sequence=sorted(nx.degree(G).values(),reverse=True)
#dmax=max(degree_sequence)
#plt.loglog(degree_sequence,'b-',marker='o')
#plt.show()
#print nx.average_clustering(G)
#print nx.average_shortest_path_length(G)
#print time.clock() - start_time
'''
