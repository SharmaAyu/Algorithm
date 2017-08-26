
from _collections import defaultdict

class Graph:
    def __init__(self,vertex):
        self.V = vertex
        self.graph = defaultdict(list)
    def addEdge(self,src,dest):
        self.graph[src].append(dest)
    def find(self,parent,i):
        if parent[i]==-1:
            return i
        if parent[i]!=-1:
            return self.find(parent,parent[i])
    def union(self,parent,x,y):
        x_set = self.find(parent,x)
        y_set = self.find(parent,y)
        parent[x_set] = y_set

    def iscycle(self):
        parent=[-1]*self.V
        
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find(parent, i)
                y = self.find(parent, j)
                if x==y:
                    return True
                self.union(parent, x, y)
g = Graph(3)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)
 
if g.iscycle():
    print ("Graph contains cycle")
else :
    print ("Graph does not contain cycle ")