


### Converting list format to adjacency matrix
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import networkx as nx
from networkx.algorithms import bipartite as bp

G=nx.Graph()

f = open('ratings_data_5000.txt')
    
triplets=f.read().split()
#print triplets
for i in range(0,len(triplets)): 
    triplets[i]=triplets[i].split(',')    
    
B=np.array(triplets, dtype=np.uint8)
print (len(B))
A=B.reshape(5000,3)
print(A)



Adjacency=np.zeros((65, 4667), dtype=np.int)
#
print(Adjacency)
#
#
for k in range(0,5000):
    Adjacency[A[k][0]-1][A[k][1]-1] = A[k][2]

print(Adjacency)
#
#
#### ploting bipartite graph using biadjacency matrix
Biadjacency = Adjacency
Biadjacency[Biadjacency > 0] = 1
#
print(Biadjacency)
print(Biadjacency.shape)
np.savetxt('Biadjacency.txt', Biadjacency, fmt='%d')
#sA = sp.sparse.csr_matrix(Biadjacency)
##print sA
#
#G=bp.from_biadjacency_matrix(sA)
#X, Y = bp.sets(G)
#pos = dict()
#pos.update( (n, (1, i)) for i, n in enumerate(X) ) # put nodes from X at x=1
#pos.update( (n, (2, i)) for i, n in enumerate(Y) ) # put nodes from Y at x=2
#nx.draw(G, pos=pos)
#
#plt.show()
