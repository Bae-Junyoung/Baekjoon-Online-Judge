HW = list(map(int,input().split()))
blocks = list(map(int,input().split()))

total = 0

for i in range(1,len(blocks)-1):
    l_max = max(blocks[:i])
    r_max = max(blocks[i:])
    
    compare = min(l_max, r_max)
    
    if blocks[i] < compare:
        total += (compare-blocks[i])

print(total)