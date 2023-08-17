T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    str_lst = [list(map(str, input())) for _ in range(N)]
    cnt = 1
    # 가로열에서 찾기
    for i in range(N):
        if cnt == 0:
            break
        for a in range(N-M+1):
            if cnt == 0:
                break
            find_str = ''
            for j in range(M):
                find_str += str_lst[i][j+a]
                new_str = ''
            for k in range(len(find_str) - 1, -1, -1):
                new_str += find_str[k]
            if new_str == find_str:
                ans = new_str
                cnt = 0
                break

    # 세로열에서 찾기
    if cnt == 1:
        for j in range(N):
            if cnt == 0:
                break
            for a in range(N - M + 1):
                if cnt == 0:
                    break
                find_str = ''
                for i in range(M):
                    find_str += str_lst[i+a][j]
                    new_str = ''
                for k in range(len(find_str) - 1, -1, -1):
                    new_str += find_str[k]
                if new_str == find_str:
                    ans = new_str
                    cnt = 0
                    break

    print(f'#{tc} {ans}')