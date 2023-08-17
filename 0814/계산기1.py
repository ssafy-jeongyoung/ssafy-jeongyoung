for tc in range(1, 11):
    N = int(input())
    sik = input()
    stack = []
    number_stack = []

    for i in range(N):
        if sik[i] == '+':
            stack.append(sik[i])
        else:
            number_stack.append(int(sik[i]))

        if i == N-1:
            for j in range(len(stack)):
                a = stack.pop()
                number_stack.append(a)

    new_stack = []
    for i in number_stack:
        if i != '+':
            new_stack.append(i)
        else:
            b = new_stack.pop()
            a = new_stack.pop()
            c = a + b
            new_stack.append(c)

    print(f'#{tc} {new_stack[0]}')
