N = int(input())

path = input()

path = ' ' + path

MAX = 999999999999
dp = [MAX] * len(path)
dp[0] = 0
dp[1] = 0

for i in range(1,len(path)):
    if path[i]=='B':
        for j in range(i,len(path)):
            if path[j]=='O':
                dp[j]=min(dp[j],dp[i]+(j-i)**2)


    elif path[i]=='O':
        for j in range(i,len(path)):
            if path[j]=='J':
                dp[j]=min(dp[j],dp[i]+(j-i)**2)

    elif path[i]=='J':
        for j in range(i,len(path)):
            if path[j]=='B':
                dp[j]=min(dp[j],dp[i]+(j-i)**2)
                
print(-1 if dp[-1]==MAX else dp[-1])