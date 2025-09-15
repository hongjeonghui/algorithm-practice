T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 최소값 구하기
    min_idx = []
    for i in range(N):
        if arr[i] == min(arr):
            min_idx.append(i)

    # 최댓값 구하기
    max_idx = []
    for i in range(N):
        if arr[i] == max(arr):
            max_idx.append(i)

    print(f'#{tc} {abs(min(min_idx)-max(max_idx))}')
