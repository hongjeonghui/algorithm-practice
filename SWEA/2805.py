T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]

    # 1. 중앙 행은 전체를 더한다.
    # 2. 그 위/아래 행은 대칭 구조이므로,
    #    중앙에서 1칸, 2칸 ... 멀어질수록 양쪽에서 잘라내고 가운데만 더한다.
    #    → 예: 중앙-1 행이면 좌우 1칸씩 제외 → arr[j : N-j]
    #    → 중앙-2 행이면 좌우 2칸씩 제외 → arr[2 : N-2]

    max_cnt = 0   # 최종 합계 저장 변수

    # 중앙 행 합산
    mid = arr[N//2]  
    for i in mid:
        max_cnt += i  

    # 중앙 기준 위쪽 절반 수확
    for j in range(1, N//2+1):
        upper = arr[N//2 - j]            # 중앙에서 위쪽으로 j칸 떨어진 행
        upper_harvest = row[j:N-j]           # 수확 범위
        for k in upper_harvest:
            max_cnt += k

    # 중앙 기준 아래쪽 절반 수확
        lower  = arr[N//2 + j]            # 중앙에서 아래쪽으로 j칸 떨어진 행
        lower_harvest = row[j:N-j]           # 수확 범위
        for k in lower_harvest:
            max_cnt += k

    print(f'#{tc} {max_cnt}')
