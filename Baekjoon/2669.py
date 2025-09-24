# 값 불러오기
arr = [list(map(int, input().split())) for _ in range(4)]

# 방문 여부 기록용
visited = [[0] * 101 for _ in range(101)]

# 각 x,y좌표 설정
for num in arr:
    x1, y1, x2, y2 = num
    for y in range(y1, y2):  # 행
        for x in range(x1, x2):  # 열
            visited[y][x] = 1

# 전체 1의 개수 
total = 0
for i in visited:
    total += i.count(1)

print(total)


# 개선된 코드
arr = [list(map(int, input().split())) for _ in range(4)]

# 방문 여부 기록용
visited = [[0] * 101 for _ in range(101)]

# 각 직사각형 좌표 채우기
for x1, y1, x2, y2 in arr:
    for y in range(y1, y2):      # 세로(y)
        for x in range(x1, x2):  # 가로(x)
            visited[y][x] = 1

# 전체 1의 개수 합산 (리스트 컴프리헨션 활용)
total = sum(row.count(1) for row in visited)

print(total)
