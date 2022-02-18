def find(x):
    global parent
    if parent[x] == x:
        return x
    else:
        return find(parent[x])
    
def Union(x,y):
    Px, Py = find(x), find(y)
    
    if Px>Py:
        parent[Px] = Py
    else:
        parent[Py] = Px
        
V, E = map(int, input().split())

graph = [[] for _ in range(V+1)]
edges = []

for _ in range(E):
    s,e,c = map(int,input().split())
    graph[s].append((c,e))
    edges.append((c,s,e))
    
edges.sort()
parent = [i for i in range(V+1)]
answer = 0

for i in edges:
    if find(i[1])==find(i[2]):
        continue
    Union(i[1], i[2])
    answer+=i[0]
    
print(answer)