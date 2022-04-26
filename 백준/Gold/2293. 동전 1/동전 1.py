n, k = map(int, input().split())

coins = []
cases = 0

for _ in range(n):
    coins.append(int(input()))
    
dp = [0] * (k+1)

for coin in coins:
    for i in range(1,k+1):
        if i==coin:
            dp[i]+=1
        
        elif i>coin:
            dp[i] += dp[i-coin]
            
print(dp[k])