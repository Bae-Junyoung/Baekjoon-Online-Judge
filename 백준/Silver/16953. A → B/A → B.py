A, B = map(int, input().split())

cnt = 1
while True:
    if A==B:
        break
    elif A>B:
        cnt=-1
        break
    elif B%10==1:
        cnt+=1
        B = B//10
    elif B%2==0:
        cnt+=1
        B = B//2
    else:
        cnt=-1
        break

print(cnt)