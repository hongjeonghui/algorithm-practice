T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    result = "NO"

    # 오른쪽, 아래, 오른쪽 아래, 오른쪽 위
    dr = [0, 1, 1, -1]
    dc = [1, 0, 1, 1]

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'o':
                for d in range(4):
                    cnt = 1
                    nr = r + dr[d]
                    nc = c + dc[d]

                    while 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 'o':
                        cnt += 1
                        nr += dr[d]
                        nc += dc[d]
                        if cnt >= 5:
                            result = "YES"
                            break

    print(f"#{tc} {result}")
