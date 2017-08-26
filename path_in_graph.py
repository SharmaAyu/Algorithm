# Python program to detect cycle 
# in a graph
 
from collections import defaultdict
 
class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices
 
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    def pathUtil(self,u, v, visited, recStack):
 
        visited[u] = True
        recStack.append(u)
        if u==v:
            print(recStack)
        else:
            for i in self.graph[u]:
                if visited[i] == False:
                    self.pathUtil(i,v, visited, recStack)
 
        # The node needs to be poped from 
        # recursion stack before function ends
        recStack.pop()
        visited[u]=False
 
    def path_node(self,u,v):
        visited = [False] * self.V
        recStack = []
        self.pathUtil(u,v,visited,recStack)
 
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.path_node(0,3)