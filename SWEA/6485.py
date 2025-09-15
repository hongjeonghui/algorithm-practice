T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 버스 노선 개수
    arr = [list(map(int, input().split())) for _ in range(N)]  # 버스 노선  [[1, 3], [2, 5]]
    P = int(input())  # 버스 정류장 개수
    bus_station = [int(input()) for _ in range(P)]  # 버스 정류장


    # 버스 정류장에 몇 개의 버스 노선이 다니는가
    visited = [0] * 5001

    for i in range(N):
        a, b = arr[i][0], arr[i][1]
        for j in range(a, b+1):
            visited[j] += 1


    result = [visited[i] for i in bus_station]
    print(f'#{tc}', *result)
