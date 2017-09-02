# This code is written for plotting degree distribution for the top nodes
import numpy as np
#import pylab as plt
#import networkx as nx
import matplotlib.pyplot as plt
#from numpy.random import uniform
#from randomgraph_epinions import calcProp
#f = open('input_1.txt')
#triplets=f.read().split()
#for i in range(0,len(triplets)): triplets[i]=triplets[i].split(',')
#B=np.array(triplets, dtype=np.uint8)
#A=B.reshape(160,2)
#print A
#Biadjacency=np.zeros((136,5), dtype=np.int)
#print Biadjacency
#for i in range(1,137):
#    for j in range(1,6):
#        for k in range(0,160):
#            if (A[k][0]==i and A[k][1]==j):
#               Biadjacency[i-1][j-1] =1
#print Biadjacency
f=open('Graph_Adj.txt')
triplets=f.read().split()
for i in range(0,len(triplets)): triplets[i]=triplets[i].split(',')
B=np.array(triplets, dtype=np.uint8)
Biadjacency=B.reshape(65, 4667)
count=0
Degree=[0]*65
#print(Degree)
for i in range(1,66):
    for j in range(1,4668):
        if (Biadjacency[i-1][j-1] ==1):
            count=count+1
    Degree[i-1]=count
    count=0
#print(Degree)
#print (max(Degree))
CountDegree=[0]*max(Degree)
probability=[0]*max(Degree)
for j in range(1, max(Degree)+1):
    for i in range(0, len(Degree)):
       if j==Degree[i]:
            CountDegree[j-1]=CountDegree[j-1]+1
#print(CountDegree)
for j in range(1, max(Degree)+1):
     probability[j-1]=float(CountDegree[j-1])/65
#print(probability)
Maxdegree=[0]*max(Degree)
for i in range(1, max(Degree)+1):
    Maxdegree[i-1]=i
#print(Maxdegree)
print('Epinions Top')
font = {'family': 'serif',
        'color':  'darkblue',
        'weight': 'normal',
        'size': 16,
        }
plt.xlabel ('Degree Value',fontdict=font)
plt.ylabel('Probability (Pk)',fontdict=font)
plt.loglog(Maxdegree,probability,'.',color='m')
plt.axis([0, 100, 0, 0.04])
#plt.grid(True,which='both')
plt.show()
