bingo = [list(map(int, input().split())) for _ in range(5)]
check = [list(map(int, input().split())) for _ in range(5)]

# 사회자가 부르는 숫자 하나의 리스트로 관리
speak = []
for i in check:
    speak.extend(i)

# 사회자가 부르는 숫자가 빙고판에 있을 경우 0으로 변환
idx = 0  # 최종 값
for num in speak:  # 사회자가 숫자를 하나씩 부를 때마다 진행
    idx += 1
    for j in range(5):
        for k in range(5):
            if num == bingo[j][k]:
                bingo[j][k] = 0


    # 빙고 줄 개수
    cnt = 0

    # 행 검사
    for r in range(5):
        row_zero = True
        for c in range(5):
            if bingo[r][c] != 0:
                row_zero = False
                break

        if row_zero:
            cnt += 1

    # 열 검사
    for c in range(5):
        col_zero = True
        for r in range(5):
            if bingo[r][c] != 0:
                col_zero = False
                break
        if col_zero:
            cnt += 1


    # 대각선
    diagonal = True
    for d in range(5):
        if bingo[d][d] != 0:
            diagonal = False
            break
    if diagonal:
        cnt += 1

    diagonal2 = True
    for d in range(5):
        if bingo[d][4-d] != 0:
            diagonal2 = False
            break
    if diagonal2:
        cnt += 1


    if cnt >=3:
        print(idx)
        break
