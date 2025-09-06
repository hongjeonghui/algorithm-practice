T = int(input())
for tc in range(1, T+1):
    # K : 최대 이동 거리, N : 정류장 수(0~N) , M : 충전기 수
    K, N, M = map(int, input().split())
    cs_num = list(map(int, input().split()))  # 충전기 있는 버스 정류장 번호

    cnt = 0
    now_pos = 0   # 현재 위치(정류장 번호)
    arrive = True  # 도착 가능 여부

    while now_pos + K < N:  # 종점 전까지
        next_pos = now_pos  # 다음 위치
        for i in range(K, 0, -1):  # 최대 충전 지점을 구하기 위해서 뒤에서 부터
            if i + next_pos in cs_num: # K칸 이내에 충전기가 있다면
                next_pos = i + now_pos  # 위치 이동
                break

        if next_pos == now_pos:   # K칸 이내에 없어서 이동이 불가능하면
            arrive = False  # 도착 불가능으로 판단
            break

        now_pos = next_pos   # 현재 위치 바꿔주기
        cnt += 1

    if arrive == True:   
        print(f'#{tc} {cnt}')
    else:
        print(f'#{tc}', 0)
