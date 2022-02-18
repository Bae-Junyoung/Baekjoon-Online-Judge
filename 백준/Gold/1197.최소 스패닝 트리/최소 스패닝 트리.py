import heapq

V, E = map(int, input().split())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    s,e,c = map(int,input().split())
    graph[s].append([e,c])
    graph[e].append([s,c])
    
answer = 0
visit = [False]*(V+1)
q = []
heapq.heappush(q, (0,1))
cnt = 0

while q:
    weight, location = heapq.heappop(q)
    if not visit[location]:
        answer+= weight
        visit[location] = True
        cnt+=1
        
        for loc,w in graph[location]:
            if not visit[loc]:
                heapq.heappush(q, (w, loc))
    
    if cnt==V:
        break
print(answer)