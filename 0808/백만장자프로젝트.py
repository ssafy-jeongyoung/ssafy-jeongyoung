# import sys
# sys.stdin = open('input.txt','r')
def search_max(lst):
    max_value = 0
    for ls in lst:
        if max_value < ls:
            max_value = ls
    return max_value

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    n_lst = list(map(int,input().split()))
    answer = 0

    while len(n_lst) > 1:
        max_price = search_max(n_lst)
        for _ in range(len(n_lst)-1, -1, -1):
            if n_lst[_] == max_price:
                del_lst = n_lst[:_+1]
                n_lst = n_lst[_+1:]
                break

        if len(del_lst) != 0:
            for i in del_lst:
                answer += max_price - i

    print(f'#{tc} {answer}')






# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     n_lst = list(map(int, input().split()))
#     perchace = 0              # 구매 비용
#     per_cnt = 0               # 구매 횟수
#     answer = 0                # 판매시 얻는 이익
#
#     for i in range(len(n_lst)):
#         max_price = search_max(n_lst)
#         if n_lst[i] == max_price:
#             if perchace != 0:           # 구매한 것이 있다면 판매
#                 answer += (max_price*per_cnt - perchace)
#                 perchace = 0           # 구매 값 초기화
#                 per_cnt = 0
#                 continue
#                 # if i != N-1:
#                 #     max_price = search_max(n_lst[i+1:]) # 현재 인덱스 이후의 값에서 최대가격을 찾음
#             else:                        # 없다면 패스
#                 continue
#             #     if i != N-1:
#             #         max_price = search_max(n_lst[i+1:])
#         else:                           # 가격이 최대값이 아니라면 구매
#             per_cnt += 1
#             perchace += n_lst[i]
#
#     print(f'#{tc} {answer}')