'''
import UserNetwork
b=UserNetwork.B
n1=len(b)
ias,ds,it=[],[],[0 for i in range(len(b[0]))]
for i in range(UserNetwork.items):
           for j in range(n1):
               if(b[j][i]==1):
                   it[i]+=1
    
it=[item for item in it if item!=0]
item=it.index(min(it))
#print(it)
#print('Least item=',item)
for p in range(n1):
      if b[p][item-1]==1:
           ias.append(p)
      else:
          ds.append(p)
'''
'''#Highest no.of items
import data_set
B=data_set.b
Degree={}
count=0
for i in range(len(B)):
    for j in range(len(B[0])):
        if (B[i][j] ==1):
            count=count+1
    Degree[i]=count
    count=0
clv=list(Degree.values())
clv.sort()
n=int(input('Enter the seed set size:'))
clv=clv[-n:]
ias,ds,nodes=[],[],[i for i in range(len(B))]
while(len(clv)!=0):
    x=clv.pop(0)
    ias.append(list(Degree.keys())[list(Degree.values()).index(x)])
    Degree.pop(list(Degree.keys())[list(Degree.values()).index(x)])
ds=list(set(nodes)-set(ias))
'''
#High Clustering Coefficient Heuristic
import numpy as np
import networkx as nx
import UserNetwork
#A=[[0,1,1,0,1,0,0,1,0,0,0],[1,0,1,1,0,1,0,0,0,1,0],[1,1,0,1,1,0,1,0,0,0,0],[0,1,1,0,0,1,1,0,0,0,0],[1,0,1,0,0,0,0,1,1,0,0],[0,1,0,1,0,0,1,0,0,1,0],[0,0,1,1,0,1,0,0,1,1,0],[1,0,0,0,1,0,0,0,1,0,0],[0,0,0,0,1,0,1,1,0,1,0],[0,1,0,0,0,1,1,0,1,0,0],[0,0,0,0,0,0,0,0,0,0,0]]  
A=UserNetwork.a
A=np.matrix(A)
G=nx.from_numpy_matrix(A)
cl=(nx.clustering(G))
clv=list(cl.values())
clv.sort()
n=int(input('Enter the seed set size:'))
clv=clv[-n:]
ias,ds,nodes=[],[],[i for i in range(len(A))]
while(len(clv)!=0):
    x=clv.pop(0)
    ias.append(list(cl.keys())[list(cl.values()).index(x)])
    cl.pop(list(cl.keys())[list(cl.values()).index(x)])
ds=list(set(nodes)-set(ias))


'''#Major Degree Heuristic
import UserNetwork
A=UserNetwork.a
Degree={}
count=0
for i in range(len(A)):
    for j in range(len(A)):
        if (A[i][j] ==1):
            count=count+1
    Degree[i]=count
    count=0
clv=list(Degree.values())
clv.sort()
n=int(input('Enter the seed set size:'))
clv=clv[-n:]
ias,ds,nodes=[],[],[i for i in range(len(A))]
while(len(clv)!=0):
    x=clv.pop(0)
    ias.append(list(Degree.keys())[list(Degree.values()).index(x)])
    Degree.pop(list(Degree.keys())[list(Degree.values()).index(x)])
ds=list(set(nodes)-set(ias))
'''