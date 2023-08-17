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
    in_str = list(input())
    stack = MyStack(len(in_str))
    for i in in_str:
        if i == '(' or i == ')' or i == '{' or i =='}':
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


################################### 다른 코드#################################
# T = int(input())
# for tc in range(1,T+1):
#     arr = input().strip()
#
#     st = []
#     flag = 0
#     for i in arr:
#         if i == "(" or i == "{":
#             st.append(i)
#         elif i == ")" or i == "}":
#             if len(st) == 0:
#                 flag = 1
#                 break
#             else:
#                 tmp = st.pop()
#                 if tmp == "(":
#                     if i != ")":
#                         flag = 1
#                 elif tmp == "{":
#                     if i != "}":
#                         flag = 1
#
#     if len(st) > 0 or flag == 1:
#         print(f"#{tc} 0")
#     else :
#         print(f"#{tc} 1")




############################# 다른코드 2 #############################
# def stack_push(item):
#     global top
#
#     top += 1
#     my_stack[top] = item
#
#
# def stack_pop():
#     global top
#
#     my_stack.pop(top)
#     top -= 1
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#
#     data = input()
#
#     SIZE = len(data)
#     top = -1
#     my_stack = [0] * SIZE
#     # 반복문을 통과했는지 확인하는 변수
#     is_result = True
#
#     for x in data:
#         # ( { 일 때
#         if x == '(' or x == '{':
#             if top >= SIZE:
#                 is_result = False
#                 break
#                 # 스택에 추가
#             stack_push(x)
#         # ) 일 때
#         elif x == ')':
#             # 빈 스택이면 틀린것이니 종료
#             if top < 0:
#                 is_result = False
#                 break
#             else:
#                 # 스택의 탑이 ( 라면 pop
#                 if my_stack[top] == '(':
#                     stack_pop()
#                 else:
#                     is_result = False
#                     break
#
#         elif x == '}':
#             # 빈 스택이면 틀린것이니 종료
#             if top < 0:
#                 is_result = False
#                 break
#             else:
#                 # 스택의 탑이 { 라면 pop
#                 if my_stack[top] == '{':
#                     stack_pop()
#                 else:
#                     is_result = False
#                     break
#
#     # 반복문은 통과했지만 스택에 괄호가 남아 있으면 틀린것
#     if is_result:
#         if top >= 0:
#             print(f'#{tc} 0')
#         # 빈 스택이면 맞음
#         else:
#             print(f'#{tc} 1')
#
#     else:
#         print(f'#{tc} 0')