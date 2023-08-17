for tc in range(1, 2):
    N = int(input())
    answer = 0               # 정답 : 회문의 갯수

    map_lst = [list(map(str, input())) for _ in range(8)]

    # 가로열에서 회문 찾기
    for i in range(8):
        for j in range(9-N):
            cnt = 0
            for k in range(N//2):
                if map_lst[i][j+k] == map_lst[i][j-k+N-1]:
                    cnt += 1
            if cnt == N//2:
                answer += 1

    # 세로열에서 회문 찾기
    for j in range(8):
        for i in range(9 - N):
            cnt = 0
            for k in range(N // 2):
                if map_lst[i+k][j] == map_lst[i-k+N-1][j]:
                    cnt += 1
            if cnt == N // 2:
                answer += 1

    print(f'#{tc} {answer}')
