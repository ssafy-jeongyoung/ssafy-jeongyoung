str_num = input()

lst = list(map(str, str_num))
sum_v = 0
for i in lst:
    if i == 'A' or i == 'B' or i == 'C':
        sum_v += 3
    elif i == 'D' or i == 'E' or i == 'F':
        sum_v += 4
    elif i == 'G' or i == 'H' or i == 'I':
        sum_v += 5
    elif i == 'J' or i == 'K' or i == 'L':
        sum_v += 6
    elif i == 'M' or i == 'N' or i == 'O':
        sum_v += 7
    elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
        sum_v += 8
    elif i == 'V' or i == 'T' or i == 'U':
        sum_v += 9
    else:
        sum_v += 10
print(sum_v)