T = int(input())

for tc in range(1, T+1):
    sudoku_map = [list(map(int, input().split())) for _ in range(9)]
    ans_cnt = 0

    # 가로열 확인
    if ans_cnt == 0:
        col_cnt = 0
        for i in range(9):
            sum_v = 0
            for j in range(9):
                sum_v += sudoku_map[i][j]
            if sum_v == 45:
                col_cnt += 1
        if col_cnt == 9:
            ans_cnt += 1

    # 세로열 확인
    if ans_cnt == 1:
        row_cnt = 0
        for j in range(9):
            sum_v = 0
            for i in range(9):
                sum_v += sudoku_map[i][j]
            if sum_v == 45:
                row_cnt += 1
        if row_cnt == 9:
            ans_cnt += 1

    # 3*3 확인
    if ans_cnt == 2:
        sq_cnt = 0
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sum_v = 0
                for k in range(3):
                    for l in range(3):
                        sum_v += sudoku_map[i+k][j+l]
                if sum_v == 45:
                    sq_cnt += 1
        if sq_cnt == 9:
            ans_cnt += 1

    if ans_cnt == 3:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')