#the Graph class contains the original graph. It is NOT meant to be modified once it's loaded.
import numpy as np
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
        for key in self.adjList:
            self.adjList[key] = tuple(self.adjList[key])
    
    def set_numVertices(self,numVertices):
        self.numVertices = numVertices
    def get_adjList(self):
        return self.adjList
    def get_numVertices(self):
        return self.numVertices