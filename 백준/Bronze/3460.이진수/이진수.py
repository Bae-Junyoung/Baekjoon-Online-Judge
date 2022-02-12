T = int(input())

for _ in range(T):
    n = bin(int(input()))[2:]
    for i,x in enumerate(n[::-1]):
        if x=='1':
            print(i, end=' ')
    print()