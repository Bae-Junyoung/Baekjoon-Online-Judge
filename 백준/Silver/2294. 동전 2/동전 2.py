n,k = map(int, input().split())

coins=[]
for _ in range(n):
    coins.append(int(input()))

dp = [0] + [10001] * (k)

coins = sorted(coins)

for coin in coins:
    for i in range(1,k+1):
        if i==coin:
            dp[i] = min(dp[i], 1)
            
        elif i>coin:
            dp[i] = min(dp[i], 1+dp[i-coin])
        
#         print(coin, i, dp)
print(dp[k] if dp[k]!=10001 else -1)