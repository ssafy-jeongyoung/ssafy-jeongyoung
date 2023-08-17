# 토너먼트 카드게임

def solve(start, end):
    if start == end:
        return start
    # start부터 end번의 학생들의 승자를 구하기 위해서
    # 절반 나누고
    m = (start + end) // 2
    winner1 = solve(start, m)
    winner2 = solve(m + 1, end)

    # w1과 w2의 결과를 반환
    if lst[winner1] == lst[winner2]:
        return winner1
    elif (lst[winner1] == 1 and lst[winner2] == 3) or (lst[winner1] == 2 and lst[winner2] == 1) or (lst[winner1] == 3 and lst[winner2] == 2):
        return winner1
    else:
        return winner2

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    result = solve(0, N-1)
    print(f'#{tc} {result+1}')