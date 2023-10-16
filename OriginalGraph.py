#the Graph class contains the original graph. It is NOT meant to be modified once it's loaded.
import numpy as np
from collections import deque
import random
import math
import pprint
class OriginalGraph: 
    def __init__(self,adjListFile,numVertices):
        self.numVertices = numVertices
        self.distanceDict = {}
        
        for i in range(self.numVertices):
            self.distanceDict[i] = None

        edges_file = open(adjListFile,"r") 
        lines = edges_file.readlines()
        edges = np.zeros((len(lines),2),dtype=int)
        for i in range(len(lines)):
            tail = (lines[i].split())[1]
            head = (lines[i].split())[2]
            edges[i] = [tail,head] 
        graph = {}
        for edge in edges:
            u,v = edge
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
            graph[v].append(u)
            
        self.adjList = graph  

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
                nodeIdx = i
            self.distanceDict[i] = distance[i]
        return nodeIdx, maxDis,
    
    def getMaxBFSDistance(self,start_node):
        maxDis = self.loadBFSTree(start_node)[1]
        return maxDis
    
    def set_numVertices(self,numVertices):
        self.numVertices = numVertices
    def get_adjList(self):
        return self.adjList
    def get_numVertices(self):
        return self.numVertices
    def get_distanceDict(self):
        return self.distanceDict