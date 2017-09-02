import math
import numpy as np
import datetime
import ias
import random
import networkx as nx
import UserNetwork
#A=[[0,1,1,0,1,0,0,1,0,0,0],[1,0,1,1,0,1,0,0,0,1,0],[1,1,0,1,1,0,1,0,0,0,0],[0,1,1,0,0,1,1,0,0,0,0],[1,0,1,0,0,0,0,1,1,0,0],[0,1,0,1,0,0,1,0,0,1,0],[0,0,1,1,0,1,0,0,1,1,0],[1,0,0,0,1,0,0,0,1,0,0],[0,0,0,0,1,0,1,1,0,1,0],[0,1,0,0,0,1,1,0,1,0,0],[0,0,0,0,0,0,0,0,0,0,0]]  
A=UserNetwork.a
seed=ias.ias
ds=ias.ds
n=len(A)
A=np.matrix(A)
G=nx.from_numpy_matrix(A)
def ShortestPathModel():
    I=[0 for i in range(len(A))] #I indicates the informed status of the nodes 
    prob=[random.uniform(0,1) for i in range(n)] #assigning probability to all nodes 
    for i in range(len(ds)):
        sp=nx.shortest_path(G,target=ds[i])#returns a dictinary to sp for shortest path from all the nodes to ds[i]
        c=math.inf #no. of shortest path nodes
        sh=0
        try:
            for s in seed:    
                if c>len(sp[s]):#finding out the seed that has shortest path to ds[i]
                    c=len(sp[s])
                    sh=s       #the seed that has the shortest path to ds[i]
            if(prob[ds[i]]<=random.uniform(0,1)):#comparing edge-weight to individual probability
                I[ds[i]] =1 #the node is informed
        except:
            I[ds[i]]=0# if the node is disconnected
        
    return(I)



R=20000    #no.of simulations
avg=[[] for i in range(R)] #list of I returned by each simulations
start=datetime.datetime.now()
for i in range(R):
    print(i)
    avg[i]=ShortestPathModel() #for each simulation the method returns the I list that represents informed status of the nodes

s=[0 for i in range(n)]#the sum of the no.of times each node got influenced out of R simulations
for i in range(n):
    for j in range(R):
        s[i]+=avg[j][i]
for i in seed:      #all seeds are set to inf
    s[i]=math.inf
end=datetime.datetime.now()
print('SPM')
print('Nodes',n)
print('Seed=',seed)
#print(s)
d={'0-4999':0,'5000-9999':0,'10000-14999':0,'15000-20000':0} #dictionary for all categories 
for a in s:
    if a>=0 and a<=4999:    #if no.of informed nodes are in the range 0-4999
        d['0-4999']=d['0-4999']+1
    if a>=5000 and a<=9999:
        d['5000-9999']=d['5000-9999']+1     #if no.of informed nodes are in the range 0-4999
    if a>=10000 and a<=14999:
        d['10000-14999']=d['10000-14999']+1 #if no.of informed nodes are in the range 0-4999
    if a>=15000 and a<=20000:
        d['15000-20000']=d['15000-20000']+1 #if no.of informed nodes are in the range 0-4999
print(d)
print('Start',start)
print('End',end)
t1=(end.minute-start.minute)*60
t2=abs(start.second-end.second)
print('Time taken',abs(t1-t2),'secs')