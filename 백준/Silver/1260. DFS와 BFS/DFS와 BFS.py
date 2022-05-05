import collections

N, M, V = map(int, input().split())

graph = collections.defaultdict(list)

for _ in range(M):
    start, end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)
    
for i in range(1,N+1):
    graph[i] = sorted(graph[i])
    
dfs_visited = []

def dfs(node):
    dfs_visited.append(node)
    for v in graph[node]:
        if v not in dfs_visited:
            dfs(v)
    return

dfs(V)
print(*dfs_visited)

from collections import deque

q = deque()
bfs_visited = []
q.append(V)
while q:
    val = q.popleft()
    bfs_visited.append(val)
    
    for v in graph[val]:
        if v not in bfs_visited:
            if v not in q:
                q.append(v)
                
print(*bfs_visited)