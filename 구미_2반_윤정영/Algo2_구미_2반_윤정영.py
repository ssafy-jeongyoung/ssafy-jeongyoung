T = int(input())

for tc in range(1, T+1):
    operation = input()
    flag = 0
    stack = []
    oper_lst = []
    for i in operation:
        if i not in '(){}':
            if oper_lst != []:
                stack.append(int(i))
            else:
                flag = 10
                break

        elif i in '({':
            stack.append(i)
            oper_lst.append(i)
        elif i == ')':
            if oper_lst[-1] == '(':
                sum_v = 0
                while stack[-1] != '(':
                    sum_v += int(stack.pop())
                stack.pop()
                oper_lst.pop()
                stack.append(sum_v)
            else:
                flag = 10
                break

        elif i == '}':
            if oper_lst[-1] == '{':
                mul_v = 1
                while stack[-1] != '{':
                    mul_v *= int(stack.pop())
                stack.pop()  # 여는 괄호 제거
                oper_lst.pop()
                stack.append(mul_v)
            else:
                flag = 10
                break
    if flag == 10:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {stack[0]}')