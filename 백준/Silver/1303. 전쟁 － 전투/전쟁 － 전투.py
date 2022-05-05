N, M = map(int, input().split())

cloths = []

for _ in range(M):
    cloths.append(list(input()))
    
    

dx = [1,0,-1,0]
dy = dx[::-1]

w_score = 0
b_score = 0

visited = [[0 for _ in range(N)] for _ in range(M)]

def dfs(y,x,color):
    visited[y][x] = 1
    cnt = 1
    
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<M and visited[ny][nx]==0:
            if cloths[ny][nx]==color:
                cnt += dfs(ny, nx, color)
                
    return cnt

for row in range(M):
    for col in range(N):
        if visited[row][col]==0:
            color = cloths[row][col]
            if color == 'W':
                w_score += dfs(row, col, color)**2
            else:
                b_score += dfs(row, col, color)**2   
        
print(w_score, b_score)