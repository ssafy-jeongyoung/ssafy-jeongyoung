for _ in range(1, 11):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]

    palindrome_len = 0

    # 가로줄 확인
    for i in range(100):
        for j in range(100):
            for k in range(100-j):
                if arr[i][j] == arr[i][99-k]:
                    cnt = 2
                    for l in range(1, (99-j-k)//2+1):
                        if arr[i][j+l] == arr[i][99-k-l]:
                            cnt += 2
                        else:
                            cnt = 0
                            break
                    if palindrome_len < cnt and (100-k-j) % 2 == 0:
                        palindrome_len = cnt
                    elif palindrome_len < cnt and (100-k-j) % 2 != 0:
                        palindrome_len = cnt-1
    # 세로줄 확인
    for j in range(100):
        for i in range(100):
            for k in range(100 - i):
                if arr[i][j] == arr[99 - k][j]:
                    cnt = 2
                    for l in range(1, (99-i-k)//2+1):
                        if arr[i+l][j] == arr[99-k-l][j]:
                            cnt += 2
                        else:
                            cnt = 0
                            break
                    if palindrome_len < cnt and (100 - k - i) % 2 == 0:
                        palindrome_len = cnt
                    elif palindrome_len < cnt and (100 - k - i) % 2 != 0:
                        palindrome_len = cnt-1

    print(f'#{tc} {palindrome_len}')

    # 1 18  (세로)
    # 2 17  (세로)
    # 3 17  (가로)
    # 4 20  (가로)
    # 5 18
    # 6 21  (세로)
    # 7 18  (가로)
    # 8 18  (세로)
    # 9 17  (세로)
    # 10 18 (세로)
