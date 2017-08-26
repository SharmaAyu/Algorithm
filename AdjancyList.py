def insertEle(adjList,src,dest):
    adjList[src].append(dest)
    
vertex = int(input())
adjList = {k: [] for k in range(vertex)}
insertEle(adjList, 0, 1)
insertEle(adjList, 0, 4)
insertEle(adjList, 1, 0)
insertEle(adjList, 1, 2)
insertEle(adjList, 1, 3)
insertEle(adjList, 1, 4)
insertEle(adjList, 4, 0)
insertEle(adjList, 4, 1)
insertEle(adjList, 4, 3)
insertEle(adjList, 3, 1)
insertEle(adjList, 3, 2)
insertEle(adjList, 3, 4)
insertEle(adjList, 2, 1)
insertEle(adjList, 2, 3)

print(adjList)




