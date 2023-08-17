T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())        # 예약 손님은 2명, 2초에 2개를 만든다
    lst = list(map(int, input().split()))      # 손님은 각각 3초, 4초에 도착
    lst.sort()
    fish_bread = 0
    ans = 0
    if lst[0] == 0:
        print(f'#{tc} Impossible')
        break
    cnt = 0         # 시간
    while True:
        cnt += 1
        if cnt % M == 0:     # 카운트가 M초가 될 때마다 붕어빵 K개 증가
            fish_bread += K

        


