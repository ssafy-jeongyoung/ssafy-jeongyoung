for tc in range(1, 2):
    N, number = map(int, input().split())
    s = str(number)
    lst = list(s)
    stack = []

    for i in lst:
        if len(stack) == 0:
            stack.append(i)
        else:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)

    sum_v = ''
    for i in range(len(stack)-1):
        sum_v += i
    print(f'#{tc} {int(sum_v)}')