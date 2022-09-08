T = int(input())

lst = []
for _ in range(T):
    lst.append(int(input()))
    
dp = [1] * (max(lst)+1)

for i in range(2,max(lst)+1):
    dp[i] += dp[i-2]
    

for i in range(3,max(lst)+1):
    dp[i] += dp[i-3]
    
for x in lst:
    print(dp[x])