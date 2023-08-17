A, B = map(int, input().split())

count = 1
while B > A:
    num = str(B)
    len_b = len(num)

    if num[len_b-1] == '1':
        B //= 10
        count += 1
        continue

    if B % 2 == 0:
        B //= 2
        count += 1
    else:
        break

if B == A:
    print(count)
else:
    print(-1)
