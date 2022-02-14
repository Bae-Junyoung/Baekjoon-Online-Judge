import sys

N = input()
An = list(map(int,input().split()))
op = list(map(int, input().split()))

maximum = -sys.maxsize
minimum = sys.maxsize

def dfs(depth, total, add, sub, mul, div):
    global maximum, minimum
    if add+sub+mul+div==0:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return
    
    if add:
        dfs(depth + 1, total + An[depth], add - 1, sub, mul, div)
    if sub:
        dfs(depth + 1, total - An[depth], add, sub - 1, mul, div)
    if mul:
        dfs(depth + 1, total * An[depth], add, sub, mul - 1, div)
    if div:
        dfs(depth + 1, int(total / An[depth]), add, sub, mul, div - 1)
    
        
dfs(1, An[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)