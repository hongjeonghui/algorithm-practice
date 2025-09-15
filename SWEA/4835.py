T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N: 정수 개수, M: 구간 개수
    arr = list(map(int, input().split()))


    total = []
    for i in range(N-M+1):
        result = sum(arr[i:i+M])
        total.append(result)

    print(f'#{tc} {max(total) - min(total)}')
