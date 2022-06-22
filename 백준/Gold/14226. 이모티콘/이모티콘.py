import collections

S = int(input())

check = [[False for _ in range(S+1)] for _ in range(S+1)]

# current[screen][board]

q = collections.deque()
time = 1
screen=1
board=1

check[screen][0] = True
check[screen][board] = True

q.append((screen, board,time))

while True:
    
    s,b,t = q.popleft()
     
    check[s][b] = min(check[s][b], t)
    
    if S==s:
        break
       
    if check[s][s]==False:
        q.append((s,s,t+1))
        check[s][s]=True
    if s+b<=S and check[s+b][b]==False:
        q.append((s+b,b,t+1))
        check[s+b][b]=True

    if s-1>=0 and check[s-1][b]==False:
        q.append((s-1,b,t+1))
        check[s-1][b]=True


print(t)