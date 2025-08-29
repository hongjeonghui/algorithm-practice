T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    score = list(map(int, input().split()))

    max_total = 0
    score = sorted(score, reverse=True)
    for i in range(K):
        max_total += score[i]

    print(f'#{tc} {max_total}')
