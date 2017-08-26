def find(parent,i):
    if parent[i]==-1:
        return i
    if parent[i]!=-1:
        return find(parent,parent[i])
def union(parent,x,y):
    x_set = find(parent,x)
    y_set = find(parent,y)
    parent[x_set] = y_set
    
parent = [-1]*5
union(parent, 0, 4)
union(parent, 4, 2)
union(parent, 1, 3)
print(find(parent,2))
print(find(parent,0))
print(find(parent,1))
    
        
    