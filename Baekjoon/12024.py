import sys
sys.stdin = open("input.txt")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            width = N  # 가능한 최대 가로 길이

            for x in range(i, N):
                if arr[x][j] == 0:
                    break

                # 현재 줄에서 가로로 몇 칸인지 1인지 확인
                current_width = 0
                for y in range(j, N):
                    if arr[x][y] == 1:
                        current_width += 1
                    else:
                        break

                # 가로 길이는 최소값 유지
                width = min(width, current_width)

                # 현재 높이에서 가능한 사각형 개수 추가
                cnt += width

print(cnt)



