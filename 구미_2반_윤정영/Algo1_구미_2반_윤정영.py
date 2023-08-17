T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]

    ans = 0  # 봉우리의 갯수

    di = [1, -1, 0, 0]      # 상하좌우 판단
    dj = [0, 0, 1, -1]
    for i in range(N):
        for j in range(N):
            max_h = maps[i][j]   # 지역의 높이(가장 커야 봉우리임)
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    if maps[ni][nj] < max_h:  # 높이가 중앙보다 낮다면
                        pass                  # 그냥 패스
                    else:                     # 중앙보다 크거나 같다면
                        max_h = -1            # 밑의 조건을 맞추기 위해 max_h 값 변경(maps[ni][nj]로 하면 값이 같은 경우 오류가 생김)
                        break                 # for문 종료
            if max_h == maps[i][j]:
                ans += 1

    print(f'#{tc} {ans}')