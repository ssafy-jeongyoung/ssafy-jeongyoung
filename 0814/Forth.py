T = int(input())

for tc in range(1, T+1):
    num_oper = input().split()
    stack = []
    for i in num_oper:
        if i == '+':
            if len(stack) >= 2:
                a = stack.pop()
                b = stack.pop()
                sum_v = b + a
                stack.append(sum_v)
            else:
                print(f'#{tc} error')
                break
        elif i == '-':
            if len(stack) >= 2:
                a = stack.pop()
                b = stack.pop()
                sum_v = b - a
                stack.append(sum_v)
            else:
                print(f'#{tc} error')
                break
        elif i == '*':
            if len(stack) >= 2:
                a = stack.pop()
                b = stack.pop()
                sum_v = b * a
                stack.append(sum_v)
            else:
                print(f'#{tc} error')
                break
        elif i == '/':
            if len(stack) >= 2:
                a = stack.pop()
                b = stack.pop()
                sum_v = b / a
                stack.append(int(sum_v))
            else:
                print(f'#{tc} error')
                break
        elif i == '.':
            if len(stack) == 1:
                print(f'#{tc} {stack[0]}')
                break
            else:
                print(f'#{tc} error')
                break
        else:   # 숫자인 경우
            stack.append(int(i))


