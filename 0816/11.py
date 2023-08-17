class MyStack:
    def __init__(self, max_size):  # 스택을 구현하기 위해 필요한 3가지
        # max_size : 최대 갯수
        self.max_size = max_size
        self.s = [None] * max_size
        self.top = -1  # 현재 스택에 들어있는 마지막 요소의 위치

    # push, pop, is_empty, is_full, peek(확인)
    def push(self, data):
        # 요소를 스택에 삽입
        self.top += 1
        self.s[self.top] = data


T = int(input())

for tc in range(1, T + 1):
    in_str = list(input())
    stack = MyStack(len(in_str))
    for i in in_str:
        if i == '(' or i == ')' or i == '{' or i == '}':
            if i == '(':
                stack.push(i)
            elif i == '{':
                stack.push(i)
            elif i == ')':
                if stack.top >= 0:
                    if stack.s[stack.top] == '(':
                        stack.top -= 1
                    else:
                        break
                else:
                    stack.top += 1
                    break
            else:
                if stack.top >= 0:
                    if stack.s[stack.top] == '{':
                        stack.top -= 1
                    else:
                        break
                else:
                    stack.top += 1
                    break

    if stack.top == -1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')