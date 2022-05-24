import collections

N, K = map(int,input().split())

parents = [-1 for _ in range(100001)]
time = [0 for _ in range(100001)]

q = collections.deque()

q.append(N)
parents[N]=-2

while q:
    current = q.popleft()
    for _next in (current-1, current+1, current*2):
        if 0<=_next<=100000 and parents[_next]==-1:
            parents[_next] = current
            time[_next] = time[current]+1
            q.append(_next)
    
#     print(q)
    
    if parents[K]!=-1:
        break
        
print(time[K])
i = K
out = [K]
while True:
    if parents[i]==-2:
        break
    out.append(parents[i])
    i = parents[i]
print(*out[::-1])