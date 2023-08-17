E, S, M = map(int, input().split())

stack_e = []
stack_s = []
stack_m = []
i = 0
while True:
    i += 1
    if i % 15 == 0:
        stack_e.append(15)
    else:
        stack_e.append(i%15)

    if i % 28 == 0:
        stack_s.append(28)
    else:
        stack_s.append(i%28)

    if i % 19 == 0:
        stack_m.append(19)
    else:
        stack_m.append(i%19)

    if stack_s[i-1] == S:
        if stack_e[i-1] == E and stack_m[i-1] == M:
            print(i)
            break

