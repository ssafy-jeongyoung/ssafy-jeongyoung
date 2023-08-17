T = int(input())

for tc in range(1, T+1):

    N = int(input())

    arr = [[0]*N for _ in range(N)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    num = 1
    d = 0           # 현재 이동하는 방향 변수
    r, c = 0, 0     # 시작점
    while True:
        if num > N*N:
            break
        # 숫자 넣고
        arr[r][c] = num
        num += 1

        # 이동할건데... 정상 범위라면 그냥 이동
        # 비정상이면 방향 바꿈
        nr = r + dr[d]
        nc = c + dc[c]
        if r + dr[d] < 0 or r + dr[d] >= N or c + dc[d] < 0 or c+dc[d] >= N \
                or arr[nr][nc] != 0:
            d = (d + 1) % 4
        # 이동하고.. 어느방향으로??  -> d를 추가
        r = r + dr[d]
        c = c + dc[d]
        # 제대로 된 인덱스라면 그대로 두고 아니라면 방향을 바꿈

    print(f'#{tc}')
    for row in arr:
        print(*row)   # 언패킹