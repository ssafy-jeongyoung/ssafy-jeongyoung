def steampack(row, film, number):  # number : 0 or 1
    for r in range(W):
        film[row][r] = number
    return None

T = int(input())

for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]

    #

