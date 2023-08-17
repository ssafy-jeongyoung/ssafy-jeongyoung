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

    def pop(self):
        # 스택에 들어있는 마지막 요소를 삭제하고 반환
        result = self.s[self.top]
        self.top -= 1   # 그냥 top만 이동시키고 나중에 삽입할 때 덮어쓰면 됨
        return result

    def is_empty(self):    # 스택이 비었으면 True
        if self.top == -1:
            return True
        return False

    def is_full(self):     # 스택이 찼으면 True
        if self.top == self.max_size-1:
            return True
        return False

    def peek(self):
        if not self.is_empty():
            return self.s[self.top]
        return None

stack = MyStack(10)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
print(stack.pop())