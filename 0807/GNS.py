T = int(input())
str_dict = {'ZRO' : 0, 'ONE' : 1, 'TWO' : 2, 'THR' : 3, 'FOR' : 4, 'FIV' : 5, 'SIX' : 6, 'SVN' : 7, 'EGT' : 8, 'NIN' : 9}
for _ in range(1, T+1):
    num_lst = [0] * 10
    tc, N = map(str, input().split())
    n = int(N)

    num_str = list(map(str, input().split()))

    for _ in range(n):
        num_lst[str_dict[num_str[_]]] += 1

    ans_lst = ''
    ans_lst += 'ZRO ' * num_lst[0]
    ans_lst += 'ONE ' * num_lst[1]
    ans_lst += 'TWO ' * num_lst[2]
    ans_lst += 'THR ' * num_lst[3]
    ans_lst += 'FOR ' * num_lst[4]
    ans_lst += 'FIV ' * num_lst[5]
    ans_lst += 'SIX ' * num_lst[6]
    ans_lst += 'SVN ' * num_lst[7]
    ans_lst += 'EGT ' * num_lst[8]
    ans_lst += 'NIN ' * (num_lst[9]-1)
    ans_lst += 'NIN'
    print(f'{tc} {ans_lst}')
#



# T = int(input())
#
# for _ in range(1, T+1):
#     tc, N = map(str, input().split())
#     str_list = list(map(str, input().split()))
#
#     str_dict = {'ZRO' : 0, 'ONE' : 1, 'TWO' : 2, 'THR' : 3, 'FOR' : 4, 'FIV' : 5, 'SIX' : 6, 'SVN' : 7, 'EGT' : 8, 'NIN' : 9}
#
#     for i in range(len(str_list)-1):
#         minIdx = i
#         for j in range(i+1, len(str_list)):
#             if str_dict[str_list[j]] < str_dict[str_list[minIdx]]:
#                 minIdx = j
#         str_list[i], str_list[minIdx] = str_list[minIdx], str_list[i]
#
#     print(f'{tc} {" ".join(str_list)}')

