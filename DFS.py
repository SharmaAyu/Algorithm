from collections import defaultdict

class Graph:
    def __init__(self,vertex):
        self.V = vertex
        self.graph = defaultdict(list)
    def addEdge(self,src,dest):
        self.graph[src].append(dest)
    def Dfs(self,src):
        visited=[False]*self.V
        self.Dfsutil(src,visited)
    def Dfsutil(self,src,visited):
        visited[src]=True
        print(src,end=" ")
        for i in self.graph[src]:
            if visited[i]==False:
                self.Dfsutil(i,visited)
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.Dfs(0)       
            
        
        