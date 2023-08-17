## 2차원 배열 순회
arr = [
    [1,1,1,0,0],
    [0,0,1,1,1],
    [1,1,1,0,0],
    [0,0,1,1,1],
    [0,0,0,0,2]
]
N = 5

def dfs():
    stack = [(0, 0)]
    visited = [[0] * N for _ in range(N)]
    visited[0][0] = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    while stack:
        cr, cc = stack[-1]
        if arr[cr][cc] == 2:
            return 1
        # 갈 수 있는 경로 모두 탐색해보기
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 0 and not visited[nr][nc]:
                stack.append((nr, nc))
                visited[nr][nc] = 1
                break
        else:
            stack.pop()

    return 0

print(dfs())