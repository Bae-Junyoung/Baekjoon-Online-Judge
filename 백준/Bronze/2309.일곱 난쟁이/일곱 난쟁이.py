lst = [int(input()) for _ in range(9)]

length = len(lst)

total = sum(lst)
first = 0
second = 0

for i in range(length):
    for j in range(i+1, length):
        if total - lst[i] - lst[j] == 100:
            n1, n2 = lst[i], lst[j]
            
            lst.remove(n1)
            lst.remove(n2)
            lst.sort()
            
            for k in lst:
                print(k)
            break
            
    if len(lst) < length:
        break