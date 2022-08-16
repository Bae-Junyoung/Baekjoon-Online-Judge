from collections import deque

N,M = map(int,input().split())

_map = []
for _ in range(N):
    _map.append(list(map(int,input().split())))

loc=[[False]*M for _ in range(N)]
lst = []
for n in range(N):
    for m in range(M):
        if _map[n][m]==1:
            loc[n][m] = True
            lst.append((n,m))
        else:
            loc[n][m] = False
            _map[n][m] = 1000

dr = [1,1,0,-1,-1,-1,0,1]
dc = [0,1,1,1,0,-1,-1,-1]

for r,c in lst:
    q = deque()
    q.append((r,c,_map[r][c]))
    while q:
        r, c, val = q.popleft()
        for i in range(8):
            if 0<=r+dr[i]<N and 0<=c+dc[i]<M and loc[r+dr[i]][c+dc[i]]!=True:
                _map[r+dr[i]][c+dc[i]] = min(_map[r+dr[i]][c+dc[i]], val+1)
                loc[r+dr[i]][c+dc[i]] = True
                q.append((r+dr[i],c+dc[i],val+1))
        
    loc=[[False]*M for _ in range(N)]
    for x,y in lst:
        loc[x][y] = True
    
print(max(list(map(max,_map)))-1)
