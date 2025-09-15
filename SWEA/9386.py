T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 수열의 길이
    arr = list(map(int, input().strip()))

    max_cnt = cnt = 0
    for i in range(N):
        if arr[i] == 1:
            cnt += 1
        else:
            max_cnt = max(cnt, max_cnt)
            cnt = 0

    if max_cnt < cnt:
        max_cnt = cnt

    print(f'#{tc} {max_cnt}')
