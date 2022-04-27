n = int(input())

comp = []
for _ in range(n):
    comp.append(list(map(int,input())))
    
from collections import deque

visits = [[0] * n for i in range(n)]

dx = [1, 0, -1, 0]
dy = dx[::-1]

bd_num = 1
res = dict()

def bfs(x, y, bd_num):
    q = deque([[x,y]])
    visits[x][y] = 1
    while q:
        node = q.popleft()
        for i in range(4):
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if visits[nx][ny] == 0 and comp[nx][ny] == 1:
                    q.append([nx,ny])
                    visits[nx][ny] = 1
                    res[bd_num] += 1
    
for i in range(n):
    for j in range(n):
        if comp[i][j]==1 and visits[i][j]==0:
            res[bd_num]=1
            bfs(i,j,bd_num)
            bd_num += 1
            
            
print(len(res))
value = sorted(res.values())

for x in value:
    print(x)    