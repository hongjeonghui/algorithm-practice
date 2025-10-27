T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 행렬 개수, 행렬 크기 (곱했을 때 작은순)

    result = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                r = 0
                while i + r < N and arr[i+r][j] != 0:
                    r += 1

                c = 0
                while j + c < N and arr[i][j+c] != 0:
                    c += 1

                for x in range(i, i + r):
                    for y in range(j, j+c):
                        arr[x][y] = 0

                result.append((r,c))

    result.sort(key=lambda x:(x[0]*x[1], x[0]))

    print(f'#{tc} {len(result)}', end=' ')
    for r, c in result:
        print(r, c, end=' ')
    print()
