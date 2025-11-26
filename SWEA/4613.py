T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    row_cost = []
    for r in range(N):
        w_cnt = 0
        b_cnt = 0
        r_cnt = 0
        line = arr[r]
        for c in line:
            if c != 'W':
                w_cnt += 1
            if c != 'B':
                b_cnt += 1
            if c != 'R':
                r_cnt += 1
        row_cost.append([w_cnt, b_cnt, r_cnt])

    answer = float('inf')
    # W 구간 : 0 ~ i
    # B 구간 : i+1 ~ j
    # R 구간 : j+1 ~ N-1
    for i in range(N-2):
        for j in range(i+1, N-1):
            cnt = 0

            # W 영역
            for r in range(0, i+1):
                cnt += row_cost[r][0]

            # B 영역
            for r in range(i+1, j+1):
                cnt += row_cost[r][1]

            # R 영역
            for r in range(j+1, N):
                cnt += row_cost[r][2]

            if cnt < answer:
                answer = cnt

    print(f'#{tc} {answer}')
