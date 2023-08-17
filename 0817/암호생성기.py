for tc in range(1, 11):
    tc = int(input())
    Q = list(map(int, input().split()))

    while Q[-1] != 0:
        for i in range(1, 6):
            Q[0] -= i
            if Q[0] <= 0:
                Q[0] = 0
                Q.append(Q.pop(0))
                break
            Q.append(Q.pop(0))

    print(f'#{tc}', *Q)