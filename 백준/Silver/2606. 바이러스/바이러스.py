import collections

N = int(input())
K = int(input())

parent = [i for i in range(N+1)]

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return x

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(K):
    a, b = map(int,input().split())
    union_parent(parent,a,b)

answer = 0
for i in range(1, N+1):
    if find_parent(parent, i) == 1:
        answer += 1

print(answer-1)