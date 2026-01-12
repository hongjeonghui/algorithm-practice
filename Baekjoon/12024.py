N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

cnt = 0

for i in range(N):
    for k in range(N):
        if i == k:
            continue

        common = 0
        for j in range(N):
            if A[i][j] == 1 and A[k][j] == 1:
                common += 1

        cnt += common * (common - 1)

print(cnt)
