import random
import math
import pprint
from OriginalGraph import OriginalGraph
from Graph import Graph

#input_graph = OriginalGraph("oldenburg edges.txt",6105)
#input_graph = OriginalGraph("san joaquin edges.txt",18263)
input_graph = OriginalGraph("san francisco edges.txt",174956)
#input_graph = OriginalGraph("california edges.txt",21047)
def shallowSeparator(G,l):
    iterations = 0

    K = [[random.randrange(0,G.get_numVertices())]] 
    S = []
    H = G
    H.removeNode(K[0][0])
    H.update_outside_adjList(K)
    while H.get_numVertices()>=2*G.OriginalGraph.get_numVertices()/3:# and iterations != 5: 
        iterations+=1
        print("iteration",iterations)
        print("--------------------------------------------")

        v = random.randrange(0,H.get_numVertices())
        T_v = H.getBFSTree(v)
        if H.getMaxBFSDistance(v) <= 2*l*math.log(G.OriginalGraph.get_numVertices()):
            C_v = H.getMinimalSubtree(v,K) # C_v = minimal subtree of T_v st all subgraphs in K neigbor it.
            print("C_v length:",len(C_v))
            K.append(C_v)
            H.update_outside_adjList(K)
            if len(K) == 6:
                return K
            for node in C_v:
                H.removeNode(node)
            largestConnectedComponent = H.getLargestConnectedComponent()
            for node in H.get_adjList():
                if node not in largestConnectedComponent:
                    H.removeNode(node)
        else:
            print("CASE TWO")
            X = H.findSeparator()
            S.append(X)
            for node in X:
                H.removeNode(node)
            largestConnectedComponent = H.getLargestConnectedComponent()
        K = H.trim(K)
        H.update_outside_adjList(K)
    for subgraph in K:
        for node in subgraph:
            S.append(node)
    return S

copy = {}
for key in input_graph.get_adjList():
    copy[int(key)] = list(input_graph.get_adjList()[key])
G = Graph(input_graph,copy)
l = math.sqrt(input_graph.get_numVertices())
x = shallowSeparator(G,l)
print("S:",x)
print("Size of S:",len(x))
