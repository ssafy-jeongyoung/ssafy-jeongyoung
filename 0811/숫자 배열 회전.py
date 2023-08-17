import sys
sys.stdin = open("input.txt", "r")
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     lst = [list(map(str, input().split())) for _ in range(N)]
#     ans_lst = [['']*3 for _ in range(N)]
#     # 90도 회전 -> 세로중앙선을 기준으로 좌우를 바꾸고 / 대각선으로 축 회전 (3번 반복)
#     for _ in range(3):      # 90, 180, 270도 회전이므로 3번 반복
#         # 좌우 바꾸기
#         for i in range(N):
#             for j in range(N//2+1):
#                 lst[i][j], lst[i][N-1-j] = lst[i][N-1-j], lst[i][j]
#         # / 대각선을 기준으로 체인지
#         cnt = N
#         for i in range(N-1):
#             cnt -= 1
#             for j in range(cnt):
#                 lst[i][j], lst[N-j-1][N-i-1] = lst[N-j-1][N-i-1], lst[i][j]
#         for i in range(N):
#             str_n = ''.join(lst[i])
#             ans_lst[i][_] += str_n
#
#     print(f'#{tc}')
#     for _ in range(N):
#         print(f'{ans_lst[_][0]} {ans_lst[_][1]} {ans_lst[_][2]}')



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [list(input().split()) for _ in range(N)]
    # ['123', '456', '789']
    print(f'#{tc}')
    for j in range(N):
        print("".join(lst[i][j] for i in range(N-1, -1, -1)), end=" ")
        print("".join(lst[N-1-j][i] for i in range(N-1, -1, -1)), end=" ")
        print("".join(lst[i][N-1-j] for i in range(N)))