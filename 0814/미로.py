def dfs(r, c, maps):
    stack = [(r, c)]
    visited = [[0] * N for _ in range(N)]
    visited[0][0] = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    while stack:
        cr, cc = stack[-1]
        if maps[cr][cc] == 3:
            return 1
        # 갈 수 있는 경로 모두 탐색해보기
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N and maps[nr][nc] != 1 and not visited[nr][nc]:
                stack.append((nr, nc))
                visited[nr][nc] = 1
                break
        else:
            stack.pop()
    return 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maps = [list(map(int, input().strip())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maps[i][j] == 2:
                row, col = i, j

    print(f'#{tc} {dfs(row, col, maps)}')

