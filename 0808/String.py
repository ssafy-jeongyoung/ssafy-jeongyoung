for _ in range(1, 11):
    tc = int(input())
    search_str = input()
    str_map = input()
    len_search = len(search_str)
    len_map = len(str_map)

    answer = 0
    k = 0
    for i in range(len_map):
        if i+k < len_map:
            if str_map[i+k] == search_str[0]:
                count = 1
                for j in range(1, len_search):
                    if i+k+j < len_map:
                        if str_map[i+k+j] == search_str[j]:
                            count += 1
                        else:
                            break
                if count == len_search:
                    answer += 1
                    k += len_search-1
            else:
                pass
    print(f'#{tc} {answer}')