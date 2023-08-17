T = int(input())

for tc in range(1, T+1):
    input_str = input()
    str_lst = list(map(str, input_str))

    new_str = ''
    for i in range(len(str_lst)-1, -1, -1):
        new_str += str_lst[i]

    if new_str == input_str:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
