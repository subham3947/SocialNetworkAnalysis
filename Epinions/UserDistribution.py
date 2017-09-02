import matplotlib.pylab as plt
import networkx as nx
def Dist(A):
    count=0
    Degree=[0 for i in range(len(A[0]))]
    #A=[[0,1,1,0,1,0,0,1,0,0],[1,0,1,1,0,1,0,0,0,1],[1,1,0,1,1,0,1,0,0,0],[0,1,1,0,0,1,1,0,0,0],[1,0,1,0,0,0,0,1,1,0],[0,1,0,1,0,0,1,0,0,1],[0,0,1,1,0,1,0,0,1,1],[1,0,0,0,1,0,0,0,1,0],[0,0,0,0,1,0,1,1,0,1],[0,1,0,0,0,1,1,0,1,0]]    
    for i in range(len(A)):
        for j in range(len(A)):
            if (A[i][j] ==1):
                count=count+1
        Degree[i]=count
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
    font = {'family': 'serif',
            'color':  'darkblue',
            'weight': 'normal',
            'size': 16,
            }
    plt.plot( Maxdegree,probability,'.')
    plt.xlabel ('Degree Value',fontdict=font)
    plt.ylabel('Probability (Pk)',fontdict=font)
    #plt.grid(True,which='both')
    #plt.grid(True)
    plt.show()
    plt.savefig("EpinionsUser.png")
def erdos(n,e):
    p=float((2*e))/float((n*(n-1)))
    EG=nx.erdos_renyi_graph(n, p)
    return EG
