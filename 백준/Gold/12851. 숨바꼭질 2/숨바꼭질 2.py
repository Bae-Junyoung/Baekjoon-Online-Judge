import collections

N, K = map(int,input().split())

loc_depth = [100001 for _ in range(100001)]
cnt = [0 for _ in range(100001)]
q = collections.deque()

q.append(N)
loc_depth[N]=0
cnt[N]=1
depth = 1

while q:
    queue = q.copy()
    for _ in queue:
        current = q.popleft()
        for _next in (current-1, current+1, current*2):
            if 0 <= _next <= 100000 and loc_depth[_next] >= depth:
                loc_depth[_next] = min(loc_depth[_next], depth)
                cnt[_next] +=1
                q.append(_next)

    
    depth+=1

    if cnt[K]!=0:
        break
        
print(loc_depth[K])
print(cnt[K])