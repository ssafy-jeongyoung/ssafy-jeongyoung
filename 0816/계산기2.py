for tc in range(1, 11):
    N = int(input())
    stack = [0] * N
    top = -1
    icp = {'*': 2, '+': 1}
    fx = input()
    susik = ''
    # 후위 표기법으로 바꿈
    for x in fx:
        if x not in '+*':
            susik += x
        else:  # '+*'
            if top == -1 or icp[stack[top]] < icp[x]:  # 토큰의 우선순위가 더 높으면
                top += 1
                stack[top] = x
            elif icp[stack[top]] >= icp[x]:
                while top > -1 and icp[stack[top]] >= icp[x]:
                    susik += stack[top]
                    top -= 1
                top += 1  # push
                stack[top] = x
    for _ in range(top+1):
        susik += stack[top]
        top -= 1


    new_stack = []
    for i in susik:
        if i not in '+*':
            new_stack.append(int(i))
        elif i == '+':
            b = new_stack.pop()
            a = new_stack.pop()
            c = a + b
            new_stack.append(c)
        elif i == '*':
            b = new_stack.pop()
            a = new_stack.pop()
            c = a * b
            new_stack.append(c)

    print(f'#{tc} {new_stack[0]}')
