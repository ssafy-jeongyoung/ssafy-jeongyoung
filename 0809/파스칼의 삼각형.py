class MyStack:
    def __init__(self, max_size):           # 스택을 구현하기 위해 필요한 3가지
        # max_size : 최대 갯수
        self.max_size = max_size
        self.s = [None] * max_size
        self.top = -1    # 현재 스택에 들어있는 마지막 요소의 위치

    # push, pop, is_empty, is_full, peek(확인)
    def push(self, data):
        # 요소를 스택에 삽입
        self.top += 1
        self.s[self.top] = data

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    stack = MyStack(N)
    for m in range(1, N+1):
        floor_lst = [1] * m
        # m = 3, 즉 3층부터 1 이외의 숫자가 나오므로
        if m > 2:
            for i in range(1, m-1):
                floor_lst[i] = stack.s[stack.top][i-1] + stack.s[stack.top][i]

        stack.push(floor_lst)
    print(f'#{tc}')
    for i in stack.s:
        print(*i)



