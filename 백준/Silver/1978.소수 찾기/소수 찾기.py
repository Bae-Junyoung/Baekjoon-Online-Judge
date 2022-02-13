N = input().split()
cnt = 0

primeN = [0,0] + [1]*999

for i in range(2,1000+1):
    for j in range(2,1000+1):
        if i*j>1000:
            break
        primeN[i*j]=0
        
nums = list(map(int,input().split()))

for x in nums:
    if primeN[x]==1:
        cnt+=1
        
print(cnt)