import data_set
B=data_set.b
#B=[[1,0,0,0],[1,1,0,0],[1,1,1,0],[0,1,0,1],[0,0,1,0]]
a=[[0 for i in range(len(B))] for i in range(len(B)) ]
items=len(B[0])
for u in range(len(B)):#each row
    for i in range(items):#each item
        if(B[u][i]==1):#if the node has that item
            for j in range(len(B)):#for column having 1's
                if(B[j][i]==1 and (j!=u)):
                    a[u][j]=1
for i in range(len(a)):
    a[i][i]=0


'''
from Algo_2_Projection import Biadjacency
#B=[[1,0,0,0,1],[1,1,1,0,0],[1,1,1,1,0],[0,0,1,0,1],[0,0,1,1,0],[0,1,1,1,0],[0,1,1,1,0],[1,0,0,1,1],[0,1,1,0,1],[1,0,1,0,1]]
B=Biadjacency
def getUser(B):
    a=[[0 for i in range(5)] for i in range(5) ]
    #items=len(B)
    for u in range(5):#each row
        for i in range(10):#each item
            if(B[i][u]==1):#if the node has that item
                for j in range(5):#for column having 1's
                    if(B[i][j]==1 and (j!=u)):
                        a[u][j]=1
    
    print(a)
    return
getUser(B)
'''