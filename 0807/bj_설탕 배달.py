N = int(input())

dp = [0] * (N+1)
dp[0] = 0
dp[1] = dp[2] = -1

for i in range(3, N+1):
    if dp[i-3] != -1:
        dp[i] = dp[i-3] + 1
        if dp[i-5] != -1:
            dp[i] = dp[i-5]+1

    else:
        if i == 4:
            dp[i] = -1
        elif dp[i-5] != -1:
            dp[i] = dp[i-5] + 1
        else:
            dp[i] = -1

print(dp[N])
