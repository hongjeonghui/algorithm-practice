N = int(input())
nums = list(map(int, input().split()))


line = []  # 줄 번호
for idx, num in enumerate(nums):
    line.append(idx+1)

    # 이동해야하는 칸 수가 0보다 크면 위치 조정
    if num > 0:
        student = line.pop()  # 맨 마지막에 들어간 번호 꺼내기
        pos = idx - num  # 이동할 위치
        # line[:pos] -> pos 앞부분, [student] -> 넣을 번호, line[pos:] -> pos부터 끝부분까지
        line = line[:pos] + [student] + line[pos:]


print(*line)



# insert 버전
N = int(input())
nums = list(map(int, input().split()))

line = []
for idx, num in enumerate(nums):
    pos = idx - num           # 들어갈 위치
    line.insert(pos, idx + 1) # 바로 삽입

print(*line)

