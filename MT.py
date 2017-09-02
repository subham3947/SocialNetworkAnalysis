import UserNetwork
import math
import random
import datetime
import ias
seed=ias.ias
#seed=[1,2,3]
ds=ias.ds
#ds=[0,4,5,6,7,8,9]
#net=[[0,1,1,0,1,0,0,1,0,0],[1,0,1,1,0,1,0,0,0,1],[1,1,0,1,1,0,1,0,0,0],[0,1,1,0,0,1,1,0,0,0],[1,0,1,0,0,0,0,1,1,0],[0,1,0,1,0,0,1,0,0,1],[0,0,1,1,0,1,0,0,1,1],[1,0,0,0,1,0,0,0,1,0],[0,0,0,0,1,0,1,1,0,1],[0,1,0,0,0,1,1,0,1,0]]    
net=UserNetwork.a
n=len(net)

Degree=[0 for i in range(len(net))] #for calculating degree for each nodes
count=0
for i in range(len(net)):
    for j in range(len(net)):
        if (net[i][j] ==1):
            count=count+1
    Degree[i]=count
    count=0
def MajorityThreshold():
    A=set(seed)
    I=[0 for i in range(len(net))] #I indicates the informed status of the nodes 
    prob=[random.uniform(0,1) for i in range(len(net))] #assigning probability to all nodes 
    
    for x in ds:    #for each node x in the ds
         N=[]       
         for p in range(n):
            if net[x][p]==1:
                 N.append(p)    #N has the adjacent nodes
         N=[c for c in N if c in A] # now N consists ony the nodes that are active
         maj=0
         for c in N:
             if prob[x]<=random.uniform(0,1): #comparing edge-weight to individual probability
                 maj+=1                      #no. of active nodes that can influence
         #maj=len([c for c in N if c in A])
         if(maj>=math.ceil(Degree[x]/2)):   #if maj has more than half of the Degree of the node
             I[x]=1                         #informed
             A.add(x)                       #add to the active set
    return(I)           
R=20000  #no.of simulations
avg=[[] for i in range(R)]  #list of I returned by each simulations
start=datetime.datetime.now()
for i in range(R):
    print(i)
    avg[i]=MajorityThreshold() #for each simulation the method returns the I list that represents informed status of the nodes
#print('Average no. of nodes that are Influenced:',sum(avg)/R)
s=[0 for i in range(n)] #sum of the no.of times a node got influenced
for i in range(n):
    for j in range(R):
        s[i]+=avg[j][i]  #the sum of the no.of times each node got influenced out of R simulations
for i in seed:          #all seeds are set to inf
    s[i]=math.inf
end=datetime.datetime.now()
print('MT')
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
print('End ',end)
t1=(end.minute-start.minute)*60
t2=abs(start.second-end.second)
print('Time taken',abs(t1-t2),'secs')