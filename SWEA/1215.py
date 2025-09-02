T = 10
for tc in range(1, T+1):
    N = int(input())  # 회문의 길이
    arr = [list(input().strip()) for _ in range(8)]
    cnt = 0

    # 가로
    for i in range(8):
        for j in range(8-N+1):
            word = arr[i][j:j+N]
            if word == word[::-1]:
                cnt += 1


    # 세로
    arr2 = list(zip(*arr))
    for i in range(8):
        for j in range(8-N+1):
            word = arr2[i][j:j+N]
            if word == word[::-1]:
                cnt += 1

    print(f'#{tc} {cnt}')
