from collections import deque
import collections

N, M = map(int, input().split())

graph = collections.defaultdict(list)
table = [0] * (N+1)

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    table[b] +=1 
    
q = deque()

for i,x in enumerate(table):
    if i!=0:
        if x==0:
            q.append(i)
            
result = []

while q:
    node = q.popleft()
    result.append(node)
    
    for v in graph[node]:
        table[v] -= 1
        
        if table[v]==0:
            q.append(v)
            
print(' '.join(map(str,result)))