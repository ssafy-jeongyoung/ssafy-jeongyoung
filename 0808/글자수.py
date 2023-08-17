T = int(input())

for tc in range(1, T+1):
    str_1 = input()
    str_2 = input()

    str1_dict = dict()
    str2_dict = dict()

    # 딕셔너리에 글자가 몇 개인지 저장
    for i in str_1:              # {'X' : 1, 'Y' : 1, 'P' : 1, 'V' : 1}
        if str1_dict.get(i) == None:
            str1_dict[i] = 1
        else:
            pass
    # {'E' : 1, 'O' : 1, 'G' : 2, 'X' : 1, 'Y' : 2, 'P' : 1, 'V' : 1, 'S' : 1}
    for i in str_2:
        if str2_dict.get(i) == None:
            str2_dict[i] = 1
        else:
            str2_dict[i] += 1

    #
    max_value = 0
    for i in str1_dict:
        if i in str2_dict:
            if max_value < str2_dict[i]:
                max_value = str2_dict[i]

    print(f'#{tc} {max_value}')
