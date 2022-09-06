import sys

N = int(input())

path = list()

for i in range(N):
#     lst = list(map(int,sys.stdin.readline().rstrip().split()))
    lst = list(map(int, input().split()))
    path.append(lst)

checked= [[0] * N for _ in range(N)]

checked[0][0]=1

for r in range(N):
    for c in range(N):
        if r==N-1 and c==N-1:
            break
        dist = path[r][c]
        
        if r + dist < N:
            checked[r+dist][c] += checked[r][c]
        if c + dist < N:
            checked[r][c+dist] += checked[r][c]
#         print(dist, checked)
        
print(checked[N-1][N-1])