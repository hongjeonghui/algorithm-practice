for tc in range(1, 11):
    _ = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]


    # 정답이 가능한 리스트
    answer_list =[]
    x_point = arr[0]
    for i, n in enumerate(x_point):
        if n == 1:
            answer_list.append(i)


    for i in answer_list:
        x = 0
        y = i # start_point
        while x < 99:
            # 왼쪽으로 이동
            if y > 0  and arr[x][y-1] == 1:
                while y > 0 and arr[x][y-1]:
                    y -= 1
                x += 1

            # 오른쪽으로 이동
            elif y < 99 and arr[x][y+1] == 1:
                while y < 99 and arr[x][y+1] == 1:
                    y += 1
                x += 1

            else:
                x += 1
        if arr[x][y] == 2:
            print(f'#{tc} {i}')
