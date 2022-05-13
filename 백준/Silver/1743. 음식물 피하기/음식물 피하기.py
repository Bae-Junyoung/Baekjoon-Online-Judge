import sys, collections

N, M, K = map(int,sys.stdin.readline().rstrip().split())

waste = [[0]*M for _ in range(N)]
check = [[0]*M for _ in range(N)]

for _ in range(K):
    r,c = map(int,input().split())
    waste[r-1][c-1] = 1

dr = [1,0,-1,0]
dc = dr[::-1]

def bfs(row,col,wasted, check):
  
    size = 1
    q = collections.deque()
    q.append((row,col))
    check[row][col] = 1
    
    while q:
        r,c = q.popleft()
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0<=nr< N and 0<=nc<M and check[nr][nc]==0 and waste[nr][nc]==1:
                size+=1
                q.append((nr,nc))
                check[nr][nc] = 1
    return size

ans = 0
for row in range(N):
    for col in range(M):
        if waste[row][col]!=0:
            ans = max(ans,bfs(row,col,waste,check))

print(ans)