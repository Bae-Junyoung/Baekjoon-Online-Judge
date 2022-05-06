import collections

N, M = map(int,input().split())

field = []

for _ in range(N):
    field.append(list(map(int,list(input()))))
    

dx = [1,0,-1,0]
dy = dx[::-1]


def bfs(r,c):
    q = collections.deque()
    q.append((r,c))
    
    while q:
        row, col = q.popleft()
        for i in range(4):
            nrow, ncol = row+dy[i], col+dx[i]
            if nrow==N-1 and ncol==M-1:
                field[nrow][ncol] = field[row][col]+1
                return
            if 0<=nrow<N and 0<=ncol<M and field[nrow][ncol]==1:
                field[nrow][ncol] = field[row][col]+1
                q.append((nrow,ncol))
                
    return
                
bfs(0,0)

print(field[N-1][M-1])