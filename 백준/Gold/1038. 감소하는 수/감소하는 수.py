n = int(input())

import itertools

pool = [0,1,2,3,4,5,6,7,8,9]
pool = list(map(str, pool))
lst = []
for i in range(1,11):
    lst += (list(map(int,list(map(lambda x: ''.join(x),list(map(lambda x: sorted(x, reverse=True),itertools.combinations(pool,i))))))))
    
print(sorted(lst)[n] if n<1023 else -1)