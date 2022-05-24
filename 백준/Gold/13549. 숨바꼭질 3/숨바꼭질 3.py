import collections

N, K = map(int,input().split())

if N>=K:
    print(N-K)
    
else:
    time = [0 for _ in range(100001)]
    check = [False for _ in range(100001)]
    
    q = collections.deque()
    q.append(N)
    check[N]=True
    
    while q:
        current = q.popleft()
        if current*2<=100000 and check[current*2]==False:
            q.appendleft(current*2)
            time[current*2] = time[current]
            check[current*2]=True
        if 0<=current-1 and check[current-1]==False:
            q.append(current-1)
            time[current-1] = time[current] + 1
            check[current-1]=True
        if current+1<=100000 and check[current+1]==False:
            q.append(current+1)
            time[current+1] = time[current] + 1
            check[current+1]=True

        
#         print(q)
        if time[K]!=0:
            break
    print(time[K])