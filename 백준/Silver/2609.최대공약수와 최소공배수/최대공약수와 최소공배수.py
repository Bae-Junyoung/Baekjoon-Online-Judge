ab = list(map(int, input().split()))
a,b = ab[0], ab[1]

while True:
    if b>a:
        a, b = b, a
    
    a, b = b, a%b
    
    if b==0:
        break
print(a)
print(int(ab[0]*ab[1] / a))
