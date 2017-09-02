import queue
from anytree import Node, RenderTree
import random
import UserNetwork
import ias
import math
import datetime
ias,ds=ias.ias,ias.ds
#ias=[1,2,3]
#ds=[0,4,5,6,7,8,9]
#Diffusion Tree Computation
A=UserNetwork.a

    #print(A)
    #A=[[0,1,0,1,1,0,0,1,0,0,0,1,1,0],[1,0,0,1,1,1,0,1,0,0,0,1,0,0],[0,0,0,1,1,1,0,1,0,1,1,1,1,0],[1,1,1,0,0,0,1,0,1,1,0,0,0,1],[1,1,1,0,0,0,0,0,0,1,0,0,0,0],[0,1,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,1,0,0,0,1],[1,1,1,0,0,0,0,0,1,1,0,0,0,0],[0,0,0,1,0,0,0,1,0,0,0,1,0,0],[0,0,1,1,1,0,1,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,1,0,0,0,0,0],[1,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,1,0,0,0,0,0,0,0]]
    #A=[[0,1,1,1,0,0,1],[1,0,1,1,0,0,0],[1,1,0,1,1,1,0],[1,1,1,0,1,1,0],[0,0,1,1,0,0,0],[0,0,1,1,0,0,0],[1,0,0,0,0,0,0]]
    #A=[[0,1,0,1,1],[1,0,0,1,1],[0,0,0,0,1],[1,1,0,0,0],[1,1,1,0,0]]
#A=[[0,1,1,0,1,0,0,1,0,0],[1,0,1,1,0,1,0,0,0,1],[1,1,0,1,1,0,1,0,0,0],[0,1,1,0,0,1,1,0,0,0],[1,0,1,0,0,0,0,1,1,0],[0,1,0,1,0,0,1,0,0,1],[0,0,1,1,0,1,0,0,1,1],[1,0,0,0,1,0,0,0,1,0],[0,0,0,0,1,0,1,1,0,1],[0,1,0,0,0,1,1,0,1,0]]    
n=len(A)
node=[i for i in range(len(A))]#all nodes    
def SingleSourceDiffusion():
    
        for r in range(len(ias)):
            for s in range(r+1,len(ias)):
                a=ias[r]
                b=ias[s]
                A[a][b]=0
        prob=[random.uniform(0.0,1.0) for i in range(len(A))] #assigning probability to all nodes 
        Q=[]
        TreeQ=[]
        DisQ=queue.Queue()
        S=[0 for i in range(len(A))]  #vector S to represent the node has been visited or not
        T=[1 for i in range(len(A))]
        for r in range(len(ias)):
            Q.append(ias[r])        #enqueue ias
            par=Node(ias[r])        #creating parent node
            TreeQ.append(par)       #enqueue ias as parent node
            DisQ.put(par)           
        n=len(A)
        I=[0 for i in range(len(A))] #I indicates the informed status of the nodes 
        while not(len(Q)==0):       #while Q is not empty
            N=[]
            v=Q.pop(0)              #v=dequeue(Q)
            if not(len(TreeQ)==0):  
                par=TreeQ.pop(0)    #par=dequeue parent
                
            for p in range(n):
                if A[v][p]==1:
                    N.append(p)     #N=all adjacent nodes to v
            if(S[v]==0):            #if v is not marked
                S[v]=1              #then mark v
                
            for b in N:             # all nodes adjacent to v 
                if(S[b]==0):        # if not visited or marked
                    if(prob[v]<=random.uniform(0.0,1.0)): #comparing edge-weight to individual probability
                        y=Node(b,parent=par)      #creating child with parent=par(line 45)
                        TreeQ.append(y)
                        S[b]=1                  #visited and marked
                        Q.append(b)             #enqueue(Q)
                        I[b]=1                  #informed
            if S==T:            #all nodes are visited or not    
                break
        return(I)

'''
   # obj=open("height.txt","w")  
        while not(DisQ.empty()):
           parent=DisQ.get()
        #parent.show()
        #obj.write(" Height of %s is "%parent)
        #obj.write(str(parent.height))
        #obj.write('\n')
        
           for pre, fill, node in RenderTree(parent):
                print("%s%s" % (pre, node.name))
    #obj.close()
 
#print('Average percent of informed nodes=',avg/20000)
'''
R=20000  #no.of simulations
avg=[[] for i in range(R)]  #list of I returned by each simulations
start=datetime.datetime.now()
for i in range(R):
    print(i)
    avg[i]=SingleSourceDiffusion()  #for each simulation the method returns the I list that represents informed status of the nodes
#print('Average no. of nodes that are Influenced:',sum(avg)/R)
s=[0 for i in range(len(A))]
for i in range(len(A)):
    for j in range(R):
        s[i]+=avg[j][i]  #the sum of the no.of times each node got influenced out of R simulations
for i in ias:           #all seeds are set to inf
    s[i]=math.inf
end=datetime.datetime.now()
print('SingleSource')
print('Nodes',n)
print('Seed=',ias)
print(s)
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
print('End ',end)
print('Time taken',abs(t1-t2),'secs')