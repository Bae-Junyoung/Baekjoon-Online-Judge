import collections

N = int(input())
M = 0

arr = [['']*N]*N

def cnt(lst):
    length = len(lst)
    count=1
    m=0
    for i in range(1,length):
        if lst[i-1]==lst[i]:
            count+=1
        else:
            m = max(m,count)
            count=1
    return max(m, count)

for i in range(N):
    row = list(input())
    arr[i] = row

for i in range(N):
    for j in range(N):
        # 동행
        if j!=N-1:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            row = arr[i]
            col_j = list(map(lambda x: x[j], arr))
            col_j1 = list(map(lambda x: x[j+1], arr))
            M = max(M, cnt(row))
            M = max(M, cnt(col_j))
            M = max(M, cnt(col_j1))
#             print('행', i,j,arr,M)
            
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]    
            
        # 동열
        if i!=N-1:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            row_i = arr[i]
            row_i1 = arr[i+1]
            col = list(map(lambda x: x[j],arr))
            M = max(M, cnt(row_i))
            M = max(M, cnt(row_i1))
            M = max(M, cnt(col))
#             print('열', i,j,arr,M)

            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
print(M)