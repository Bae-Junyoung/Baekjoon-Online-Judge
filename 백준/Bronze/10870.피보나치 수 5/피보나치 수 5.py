N = int(input())

def fib(N):
    if N<=1:
        return N
    else:
        return fib(N-1) + fib(N-2)
    
print(fib(N))