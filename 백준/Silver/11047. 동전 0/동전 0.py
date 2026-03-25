N, K = map(int, input().split())

arr = [int(input()) for _ in range(N)]

cnt = 0
for i in range(N - 1, -1, -1):
    cnt += K // arr[i]
    K = K % arr[i]

print(cnt)