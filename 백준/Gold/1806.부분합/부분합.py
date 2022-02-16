import sys

N, S = map(int, input().split())

lst = list(map(int, input().split()))

left, right = 0,1
minimum = sys.maxsize

total = lst[0]

while ((left<=right) & (right<=N)):
    if minimum==1:
        break
    if (right==N) & (total<S):
        break
    if left==N-1:
        if total>=S:
            minimum = 1
        break
    if total >= S:
        minimum = min(minimum, right-left)
        total -= lst[left]
        left+=1
    else:
        total += lst[right]
        right += 1
    
print(0) if  minimum==sys.maxsize else print(minimum)
