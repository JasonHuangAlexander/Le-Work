import numpy as np
from collections import deque
import random
import math
import pprint
from OriginalGraph import OriginalGraph
from Graph import Graph

def shallowSeparator(G,l):
    iterations = 0

    K = [[random.randrange(0,G.get_numVertices())]]
    S = []
    H = G
  
    while H.get_numVertices()>=2*G.OriginalGraph.get_numVertices()/3 and iterations != 1: 
        iterations+=1
        print("iteration",iterations)
        print("--------------------------------------------")


        v = random.randrange(0,H.get_numVertices())
        T_v = H.getBFSTree(v)
        if H.getMaxBFSDistance(v) <= 2*l*math.log(G.OriginalGraph.get_numVertices()):
            C_v = H.getMinimalSubtree(v,K) # C_v = minimal subtree of T_v st all subgraphs in K neigbor it.
            K.append(C_v)
            if len(K) == 6:
                return K
            for node in C_v:
                H.removeNode(node)
            largestConnectedComponent = H.getLargestConnectedComponent()
            for node in H.get_adjList():
                if node not in largestConnectedComponent:
                    H.remove(node)
        else:
            X = H.findSeparator()
            S.append(X)
            for node in X:
                H.removeNode(node)
            largestConnectedComponent = H.getLargestConnectedComponent()
        K = H.trim(K)
    for subgraph in K:
        for node in subgraph:
            S.append(node)
    return S

  

oldenburg_graph = OriginalGraph("oldenburg edges.txt",6105)
G = Graph(oldenburg_graph,oldenburg_graph.get_adjList())
l = math.sqrt(oldenburg_graph.get_numVertices())
x = shallowSeparator(G,l)
print(x)
