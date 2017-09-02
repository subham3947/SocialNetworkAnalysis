import networkx as nx
#Degree distribution
#Clustering Coefficient
def clusterCoeff(G):
    print('Clustering Coefficient of the graph=',nx.average_clustering(G))
    return
#Average Distance between two nodes and
#Existence of a Giant component
def GiantComponent(G):
    Gc1 = max(nx.connected_component_subgraphs(G), key=len)
    Gc=list(sorted(nx.connected_components(G), key = len, reverse=True))
    print('No. of nodes in the giant components of the graph=',len(Gc[0]))
    print('Average shortest path length=',nx.average_shortest_path_length(Gc1))
    return
#Density
def density(n,e):
    den=n*(n-1)/2
    print('Density of the graph is',e/den)
def erdos(n,e):
    p=float((2*e))/float((n*(n-1)))
    EG=nx.erdos_renyi_graph(n, p)
    print('Properties of the Erdos graph:-')
    clusterCoeff(EG)
    GiantComponent(EG)
    node=int(len(EG))
    edge=EG.number_of_edges()
    density(node,edge)
    return