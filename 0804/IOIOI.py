# 백준 #string *S1 5525번.IOIOI
def IOIOI(o_num):
    P = 'I'
    for _ in range(o_num):
        P += 'OI'
    return P

N = int(input())      #  1
M = int(input())      #  13
S = input()           #  OOIOIOIOIIOII

P_n = IOIOI(N)
stack = []
answer = 0
IOI_cnt = 0

for i in range(1, M-1):
    if S[i-1] == 'I' and S[i] == 'O' and S[i+1] =='I':
        IOI_cnt += 1
        if IOI_cnt == N:
            answer += 1
            IOI_cnt -= 1

    elif S[i-1] == 'O' and S[i] == 'I' and S[i+1] =='O':
        continue

    else:
        IOI_cnt = 0
print(answer)