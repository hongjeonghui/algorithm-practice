T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    time = list(map(int, input().split()))
    time.sort()

    possible = True
    for i in range(N):
        person_time = time[i]

        # 그 시점까지 만들어진 총 붕어빵 개수
        made = (person_time // M) * K

        # 지금까지 온 사람 수는 i + 1
        if made < i + 1:
            possible = False
            break

    if possible:
        print(f'#{tc} Possible')
    else:
        print(f'#{tc} Impossible')
