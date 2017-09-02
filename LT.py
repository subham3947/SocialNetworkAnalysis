import UserNetwork
import random
import datetime
import ias
import math
seed=ias.ias
#seed=[1,2,3]
#net=[[0,1,1,0,1,0,0,1,0,0],[1,0,1,1,0,1,0,0,0,1],[1,1,0,1,1,0,1,0,0,0],[0,1,1,0,0,1,1,0,0,0],[1,0,1,0,0,0,0,1,1,0],[0,1,0,1,0,0,1,0,0,1],[0,0,1,1,0,1,0,0,1,1],[1,0,0,0,1,0,0,0,1,0],[0,0,0,0,1,0,1,1,0,1],[0,1,0,0,0,1,1,0,1,0]]    
net=UserNetwork.a

n=len(net)

Degree=[0 for i in range(len(net))] #for calculating Degree of each nodes
count=0
for i in range(len(net)):
    for j in range(len(net)):
        if (net[i][j] ==1):
            count=count+1
    Degree[i]=count                 #Degree for ith node
    count=0
for i in range(len(net)):       #for replacing 1 with the probability in the adjacency matrix such that sum of all probabilities is 1 
    rand=[]                                             
    rand=[random.uniform(0,10)for k in range(Degree[i])] #generate random numbers within 1-10 for each node
    s=sum(rand)     #sum of the random nos.
    rand=[k/s for k in rand]    #list of probabilities with sum equals 1
    for j in range(len(net)):
        if(net[i][j]==1):       
            net[i][j]=rand.pop(0)   #replacing 1 with probability
def SingleDiffusion():
    Q,A=[],set()
    prob=[random.uniform(0,1) for i in range(len(net))] #assigning probability to all nodes 
    I=[0 for i in range(len(net))] #I indicates the informed status of the nodes 
    for i in range(len(seed)):
        Q.append(seed[i])       #enqueue to Q all the seed nodes
        A.add(seed[i])          #enqueue to active set all the seed nodes
        f =0
        while len(Q)!=0:            
            x = Q.pop(0)        #dequeing from Q
            N=[]                #all nodes adjacent to x
            for p in range(n):
                if net[x][p]!=0:
                    N.append(p)
            for v in N:         #for each v in N
                if(v not in A and prob[v]<=net[v][x]): #comparing edge-weight to individual probability
                    Q.append(v)     #enqueue to Q
                    A.add(v)        #add to the active set
                    f = f+1
                    I[v] =1         #informed
    return(I)

R=20000  #no.of simulations
avg=[[] for i in range(R)]  #list of I returned by each simulations
start=datetime.datetime.now()
for i in range(R):
    print(i)
    avg[i]=SingleDiffusion()  #for each simulation the method returns the I list that represents informed status of the nodes
#print('Average no. of nodes that are Influenced:',sum(avg)/R)
s=[0 for i in range(n)]
for i in range(n):
    for j in range(R):
        s[i]+=avg[j][i]  #the sum of the no.of times each node got influenced out of R simulations
for i in seed:          #all seeds are set to inf
    s[i]=math.inf
end=datetime.datetime.now()
print('LT')
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
t1=(end.minute-start.minute)*60
t2=abs(start.second-end.second)
print('Start',start)
print('End',end)
print('Time taken',abs(t1-t2),'secs')