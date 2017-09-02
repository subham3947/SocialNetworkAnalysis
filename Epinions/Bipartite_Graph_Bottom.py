import numpy as np
import pylab as plt

#import networkx as nx
#f = open('input_6.txt')
#triplets=f.read().split()
#for i in range(0,len(triplets)): triplets[i]=triplets[i].split(',')
#B=np.array(triplets, dtype=np.uint8)
#A=B.reshape(89,2)
#print A
##print  A.shape
#Biadjacency=np.zeros((18,14), dtype=np.int)
#for i in range(1,19):
#    for j in range(1,15):
#        for k in range(0,89):
#            if (A[k][0]==i and A[k][1]==j):
#               Biadjacency[i-1][j-1] =1
#print Biadjacency
f = open('Graph_Adj.txt')
triplets=f.read().split()
for i in range(0,len(triplets)): triplets[i]=triplets[i].split(',')
B=np.array(triplets, dtype=np.uint8)
#B=np.array(triplets, dtype='int')
Biadjacency=B.reshape(65, 4667)
count=0
Degree=[0]*4667
#print(Degree)
for i in range(1,4668):
    for j in range(1,66):
        if (Biadjacency[j-1][i-1] ==1):
            count=count+1
    Degree[i-1]=count
    count=0
#print(Degree)
#print(max(Degree))
CountDegree=[0]*max(Degree)
probability=[0]*max(Degree)
for j in range(1, max(Degree)+1):
    for i in range(0, len(Degree)):
       if j==Degree[i]:
            CountDegree[j-1]=CountDegree[j-1]+1
#print(CountDegree)
for j in range(1, max(Degree)+1):
     probability[j-1]=float(CountDegree[j-1])/4667
#print(probability)
Maxdegree=[0]*max(Degree)
for i in range(1, max(Degree)+1):
    Maxdegree[i-1]=i
#print(Maxdegree)
print('Epinions Bottom')
font = {'family': 'serif',
        'color':  'darkblue',
        'weight': 'normal',
        'size': 16,
        }
plt.loglog( Maxdegree,probability,'.')
plt.xlabel ('Degree Value',fontdict=font)
plt.ylabel('Probability (Pk)',fontdict=font)
#plt.grid(True)
#plt.grid(True)
plt.show()
