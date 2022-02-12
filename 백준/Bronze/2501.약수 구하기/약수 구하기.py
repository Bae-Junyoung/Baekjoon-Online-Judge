nk = list(map(int, input().split()))
divisor = []

def func(N, K):
    for i in range(1,N+1):
        if N%i==0:
            K = K-1
            
        if K==0:
            return i
    return 0

try:
    print(func(nk[0], nk[1]))
except IndexError:
    print(0)