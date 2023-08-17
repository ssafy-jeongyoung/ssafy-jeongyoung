T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    max_l = 0

    di = [1, 0]
    dj = [0, 1]

    for i in range(N):
        for j in range(M):
            if lst[i][j] == 1:
                for a in range(2):
                    cnt = 1
                    for k in range(1, 101):
                        ni = i + di[a] * k
                        nj = j + dj[a] * k
                        if ni == N or nj == M:
                            if max_l < cnt:
                                max_l = cnt
                            break
                        if lst[ni][nj] == 1:
                            cnt += 1
                        elif lst[ni][nj] == 0:
                            if max_l < cnt:
                                max_l = cnt
                                break

    print(f'#{tc} {max_l}')