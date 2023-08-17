def solve(row, n, sum_v):
    global result
    if result < sum_v:      # 백트래킹
        return
    if row == n:
        if result > sum_v:
            result = sum_v
        return

    for col in range(n):        # 열을 하나씩 돌면서
        if not used[col]:       # 열이 1이 아니라면
            used[col] += 1
            solve(row+1, n, sum_v+lst[row][col])
            used[col] -= 1


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    result = 100000
    used = [0] * N
    solve(0, N, 0)
    print(f'#{tc} {result}')