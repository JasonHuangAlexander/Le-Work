#the Graph class contains the original graph. It is NOT meant to be modified once it's loaded.
import numpy as np
from collections import deque
import random
import math
import pprint
class Graph: 
    def __init__(self,OriginalGraph,adjList):
        self.numVertices = len(adjList)
        self.distanceDict = {}
        self.adjList = adjList 
        self.OriginalGraph = OriginalGraph
        self.outside_adjList = {}
        for i in range(self.numVertices):
            self.distanceDict[i] = None
    
    def removeNode(self,node): 
        #del self.adjList[node]
        #self.numVertices = len(self.adjList)
        self.adjList[node] = []
    
        #remove instances of node from adjList
        for vertex in self.adjList:
            for neighbor in self.adjList[vertex]:
                if neighbor == node:
                    self.adjList[vertex].remove(neighbor)

    def getMinimalSubtree(self,v,K):
        minimalSubtree = []
        found = [False for i in range(len(K))]
        for layer in self.getBFSTree(v):
            for layer_node in self.getBFSTree(v)[layer]:
                for subgraph in K:
                    if K.index(subgraph) == False:
                        for subgraph_node in subgraph:
                            if layer_node in list(dict.keys(self.outside_adjList)):
                                if subgraph_node in self.outside_adjList[layer_node]:
                                    found[K.index(subgraph)]=True
                                    minimalSubtree.append(self.getShortestPath(v,layer_node))
        return minimalSubtree

    def getShortestPath(self,start,end): #returns a list of nodes which make up the shortest path between a start and end node.
        pred=[0 for i in range(self.numVertices)]
        dist=[0 for i in range(self.numVertices)]
        queue = [] 
        visited = [False for i in range(self.numVertices)]
        for i in range(self.numVertices):
            dist[i] = 1000000
            pred[i] = -1
        visited[start] = True
        dist[start] = 0
        queue.append(start)
        while (len(queue) != 0):
            u = queue[0]
            queue.pop(0)
            for i in range(len(self.adjList[u])):
                if (visited[self.adjList[u][i]] == False):
                    visited[self.adjList[u][i]] = True
                    dist[self.adjList[u][i]] = dist[u] + 1
                    pred[self.adjList[u][i]] = u
                    queue.append(self.adjList[u][i])
                    if (self.adjList[u][i] == end):
                        break
        path = []
        crawl = end
        path.append(crawl)
        while (pred[crawl] != -1):
            path.append(pred[crawl])
            crawl = pred[crawl]
        path.reverse()
        return path
        

    def loadBFSTree(self, start): 
        visited = [False for i in range(self.numVertices)]
        distance = [-1 for i in range(self.numVertices)]
        distance[start] = 0
        queue = deque()
        queue.append(start)
        visited[start] = True
        while queue:
            front = queue.popleft()
            for i in self.adjList[front]:
                if visited[i] == False:
                    visited[i] = True
                    distance[i] = distance[front]+1
                    queue.append(i)
        maxDis = 0
        for i in range(self.numVertices):
            if distance[i] > maxDis:
                maxDis = distance[i]
                #nodeIdx = i
            self.distanceDict[i] = distance[i]
        return maxDis #originally returned: nodeIdx, maxDis


    def getBFSTree(self,start):
        treeDict = {}
        for i in range(self.getMaxBFSDistance(start)+1):
            treeDict[i] = []
        self.loadBFSTree(start)
        for key in self.distanceDict:
            if self.distanceDict[key] != -1:
                treeDict[self.distanceDict[key]].append(key)
        return treeDict
    
    def getMaxBFSDistance(self,start_node):
        maxDis = self.loadBFSTree(start_node)#[1]
        return maxDis
    
    def getLargestConnectedComponent(self):
        adjListDict = {}
        for node in self.adjList:
            adjListDict[node] = self.adjList[node]
    
        connectedComponents = {} #dict containing each connected component
        for key in adjListDict:
            if adjListDict[key] != False:
                connectedComponents[key] = []
                currentTree = self.getBFSTree(key) 
                for layer in currentTree:
                    for node in currentTree[layer]:
                        connectedComponents[key].append(node)     
                        adjListDict[node] = False
                
        #now, return largest of the connected components
        largestComponentKey = None
        for component in connectedComponents:
            if largestComponentKey == None:
                largestComponentKey = component
            else:
                if len(connectedComponents[component]>len(connectedComponents[largestComponentKey])):
                    largestComponentKey = component
        return connectedComponents[largestComponentKey]

    def findSeparator(self):
        # find X s.t. |X| is between 0 and (|V(H)|-|largest connected component of (H-V(X))|)/l, inclusive
        count = 0
        for starting_node in self.adjList:
            node_tree = self.getBFSTree(starting_node)
            for layer in node_tree:
                count = count + len(node_tree[layer])
                if count == self.numVertices//2:
                    return node_tree[layer]
    
    def trim(self,K):
        for subgraph in K: 
            found = False
            for node in subgraph:
                for key in self.outside_adjList:
                    if node in self.outside_adjList[key]:
                        found = True
            if not found:
                K.remove(subgraph)
        return K
            
    def set_numVertices(self,numVertices):
        self.numVertices = numVertices
    def set_outside_adjList(self,outside_adjList):
        self.outside_adjList = outside_adjList
    def get_outside_adjList(self):
        return self.outside_adjList
    def get_adjList(self):
        return self.adjList
    def get_numVertices(self):
        return self.numVertices
    def get_distanceDict(self):
        return self.distanceDict