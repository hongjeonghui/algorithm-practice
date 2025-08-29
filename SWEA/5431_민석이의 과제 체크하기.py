T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))

    total = []
    for i in range(1, N+1):
        if i not in nums:
            total.append(i)


    print(f'#{tc}', *total)
