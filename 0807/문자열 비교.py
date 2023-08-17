T = int(input())

for tc in range(1,T+1):
    str_1 = input()
    str_2 = input()
    ans = 0
    for i in range(len(str_2)-len(str_1)+1):
        cnt = 0
        if str_2[i] == str_1[0]:
            cnt += 1
            for k in range(1, len(str_1)):
                if str_1[k] == str_2[i+k]:
                    cnt += 1
            if cnt == len(str_1):
                ans = 1
                break
    if ans == 0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')



# T = int(input())
#
# for tc in range(1,T+1):
#     str_1 = input()
#     str_2 = input()
#
#     if str_1 in str_2:
#         print(f'#{tc} 1')
#     else:
#         print(f'#{tc} 0')
