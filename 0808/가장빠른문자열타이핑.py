T = int(input())

for tc in range(1, T+1):
    A, B = input().split()
    count = 0
    k = 0
    for i in range(len(A)):                # A의 글자 하나하나 판단
        if i+k < len(A):                   # index 오류막기용 조건
            if A[i+k] == B[0]:             # A B의 첫 글자가 같다면
                cnt = 1                    # 카운트 +1
                for j in range(1, len(B)): # 그 다음글자를 비교
                    if i+k+j < len(A):     # index 오류막기용 조건
                        if A[i+k+j] == B[j]:
                            cnt += 1       # 같으면 카운트 +1
                        else:
                            break
                if cnt == len(B):          # 카운트가 B 글자 수와 같으면 문자수 +1
                    count += 1
                    k += len(B)-1          # index 뛰어넘기
                else:
                    count += 1             # 카운트가 다르면 문자수 +1
            else:
                count += 1                 # A와 B 첫 글자가 다르면 문자수 +1
        else:
            break                          # A의 글자를 다 훑었으면 반복문 종료
    print(f'#{tc} {count}')