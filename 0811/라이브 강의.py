# # 1. 스도쿠 검증
# def sudoku(arr):
#     for i in range(9):
#         cnt = [0] * 10
#         for j in range(9):
#             cnt[arr[i][j]] += 1
#         for k in range(1, 10):
#             if cnt[k] == 0:
#                 return 0
#
# T = int(input())
# for tc in range(1, T+1):
#     arr = [list(map(int, input().split())) for _ in range(9)]
#
#     ans = sudoku(arr)  # 스도쿠가 완성되면 1, 아니면 0
#     print(f'#{tc} {arr}')


## 2. 비밀번호
# for tc in range(1, 11):
#     str_N, str_num = input().split()
#
#     N = int(str_N)
#     stack = [0]*N
#     top = -1
#
#     for t in str_num:
#         if top == -1 or stack[top] != t: # 스택이 비어있거나 , top원소와 다르면
#             top += 1
#             stack[top] = t   # push(t)
#         else: # 스택이 비어있지 않고, top와 같으면
#             top -= 1
#
#     ans = ''.join(stack[:top+1])
#     print(f'#{tc} {ans}')

# 3. 백만장자 프로젝트
# T = int(input().split())
# for tc in range(1,T+1):
#     N = int(input())
#     lst = list(map(int, input()))




# 4. 쇠막대기




# # 5. 종이 붙이기
# def solve(N):
#     if N == 10:
#         return 1
#     elif N == 20:
#         return 3
#     else:
#         return solve(N-20)*2 + solve(N-10)
#

# 6. 길 찾기
def solve(g):
    stack = [0]
    visited = [0] * 100
    visited[0] = 1
    while stack:
        top = stack[-1]
        if top == 99:
            return 1
        for next in g[top]:
            if next != -1 and not visited[next]:
                stack.append(next)
                visited[next] = 1
                break
        else:      # 길 없음
            stack.pop()
    return 0


for _ in range(10):
    tc, E = map(int, input().split())
    V = 100
    edges = list(map(int, input().split()))
    g = [[-1]*2 for _ in range(100)]

    for i in range(0, E*2, 2):
        if g[edges[i]][0] == -1:             # 0번이 비었으면 넣고,
            g[edges[i]][0] = edges[i+1]
        else:                                # 아니면 1번에 넣는다.
            g[edges[i]][1] = edges[i+1]


    result = solve(g)
    print(f'#{tc} {result}')

