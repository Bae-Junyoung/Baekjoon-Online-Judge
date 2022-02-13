M = int(input())
N = int(input())

lst_prime = []

for i in range(M, N+1):
    isPrime = True
    if i>1:
        for j in range(2,i):
            if i%j==0:
                isPrime=False
                break
        if isPrime==True:
            lst_prime.append(i)
        
if len(lst_prime)==0:
    print(-1)
else:
    print(sum(lst_prime))
    print(min(lst_prime))