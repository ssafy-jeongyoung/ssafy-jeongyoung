n = int(input())
wine_lst = [0]
for _ in range(n):
    wine_lst.append(int(input()))   # [6, 10, 13, 9 , 8, 1]

dp = [[0, 0, 0] for _ in range(n+1)]
dp[1][1] = wine_lst[1]

if n > 1:
    for i in range(2, n+1):
        dp[i][0] = max(dp[i-1])
        dp[i][1] = dp[i-1][0] + wine_lst[i]
        dp[i][2] = dp[i-1][1] + wine_lst[i]

max_v = max(dp[n])
print(max_v)

# i = 1 : [0, 6, 0]
# i = 2 : [6, 10, 16]
# i = 3 : [16, 19, 23]
# i = 4 : [23, 25, 28]
# i = 5 : [28, 31, 33]
# i = 6 : [33, 29, 32]