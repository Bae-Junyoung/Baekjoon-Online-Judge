AB = list(map(int,input().split()))

A, B = AB[0], AB[1]

lst = [0]
for j in range(0,46):
    for k in range(j):
        lst.append(j)
        
print(sum(lst[A:B+1]))