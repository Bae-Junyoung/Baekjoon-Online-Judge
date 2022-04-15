S = int(input())

sum=0
i=1

while True:
    sum += i
    i+=1
    if sum==S:
        break
    if sum> S:
        i-=1
        break
    
print(i-1)