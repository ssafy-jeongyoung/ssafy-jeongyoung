T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())           #  3,   5
    cheese = list(map(int, input().split()))   # 7, 2, 6, 5, 3
    Q = [0] * N
    idx = 0              # 화덕에 넣을 피자 인덱스

    for _ in range(N):   # 1번 피자부터 차례차례 넣어줌
        Q[_] = idx
        idx += 1
    cheese[Q[0]] //= 2          # 다 넣었으면 처음 넣은건 한바퀴 돌았으므로 2로 나눔

    cnt = N-1                  # 후반에 쓸 카운트
    while True:
        if idx < M:             # idx가 M이 되면 피자는 남는 것 없이 다 들어가있음
            if cheese[Q[0]] != 0: # 확인했는데 치즈양이 0이 아니면
                Q.append(Q.pop(0)) # 다시 돌림
                cheese[Q[0]] //= 2 # 다음 피자를 꺼내 확인. 치즈양 2로 나눔
            else:                  # 치즈양이 0이면
                Q[0] = idx         # 다음 피자를 넣고
                idx += 1           # 대기하는 피자 인덱스 1증가

        else:                      # 피자가 다 들어가있음
            Q.append(Q.pop(0))     # 피자판을 돌리고
            if Q[0] != M:          # 치즈양이 M이 아니면(빈 화덕이 아니면)
                cheese[Q[0]] //= 2  # 치즈양 2로 나눔
                if cheese[Q[0]] == 0:  # 나눈 양이 0이 되면
                    cnt -= 1          # 카운트 하나 줄이고
                    Q[0] = M           # 피자 빼내고 빈 화덕 만듬
                if cnt == 0:          # 남은 피자가 1개라면
                    for k in range(N):  # 화덕을 조사해서
                        if Q[k] != M:    # M이 아닌 인덱스를 찾는다
                            ans = Q[k]
                    break                # while문 종료

    print(f'#{tc} {ans+1}')          # 0번 인덱스가 1번 피자이므로 +1해서 결과 출력