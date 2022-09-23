N, K = map(int,input().split(' '))
W, V = [], []

for _ in range(N):
    w, v = map(int,input().split(' '))
    W.append(w)
    V.append(v)
    
MAX = 99999999
table = [[MAX]*(K+1) for _ in range(len(W)+1)]
table[0] = [0]*(K+1)

for i in range(len(W)):
    table[i+1][0] = 0
    
for i,(w,v) in enumerate(zip(W,V)):
    for j in range(1,K+1):
        if j-w>=0:
            table[i+1][j] = max(table[i][j-w]+v, table[i][j])
        else:
            table[i+1][j] = table[i][j]
            
print(table[len(W)][K])