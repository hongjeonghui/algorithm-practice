T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 당근 개수
    nums = list(map(int, input().split()))  # 당근 크기

    max_cnt = 1  # 최대 길이
    cnt = 1
    for j in range(N-1):  # 앞 뒤 비교하기 떄문에 N-1
        if nums[j] < nums[j+1]:  # 커지는 경우
            cnt += 1
        else:  # 아닌 경우
            max_cnt = max(max_cnt, cnt)  # 최대 길이 갱신
            cnt = 1  # cnt 초기화

    if max_cnt < cnt:  # 최종 최대 길이 갱신
        max_cnt = cnt
    print(f'#{tc} {max_cnt}')



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    cnt = max_cnt = 1
    for j in range(N-1):
        if nums[j] < nums[j+1]:
            cnt += 1          # 증가면 누적
        else:
            cnt = 1           # 끊기면 리셋
        max_cnt = max(max_cnt, cnt)  # 매번 한 번만 갱신

    print(f'#{tc} {max_cnt}')
