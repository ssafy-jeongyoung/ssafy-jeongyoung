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

T = int(input())

for tc in range(1, T+1):
    in_str = list(input())

    stack = MyStack(len(in_str))
    for i in in_str:
        if i == stack.s[stack.top]:
            stack.top -= 1
        else:
            stack.push(i)

    print(f'#{tc} {stack.top+1}')



################# 다른 코드 #####################
# T = int(input())
# for tc in range(1, T + 1):
#     text = list(input())  # 리스트로 문자열을 받고
#
#     stack = []  # 스택을 만들 빈 리스트 생성
#     for txt in text:
#         # 일단은... 아무것도 없으면 push(0이면)
#         if len(stack) == 0:
#             stack.append(txt)
#         # 뭐라도 있으면 같은 문자일때와 다른 문자일때가 있을 것
#         else:
#             # 지금 검사하는 문자 == 맨 마지막에 가져오는 문자
#             if txt == stack[-1]:
#                 # 같은 건 제거해주어야 하니 pop()
#                 stack.pop()
#             else:
#                 # 다르면 그대로 stack 리스트에 추가
#                 stack.append(txt)
#
#     print(f'#{tc} {len(stack)}')
