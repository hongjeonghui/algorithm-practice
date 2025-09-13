T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    result = []  # 곱한 숫자
    total = []  # 단조에 해당하는 숫자

    for i in range(N):
        for j in range(i+1, N):
            result.append(arr[i]*arr[j])

    for k in result:
        num = k
        prev = 10 # 처음 비교 기준(맨 끝 자리보다 항상 큰 값)
        while num > 0:
            digit = num % 10  # 현재 자릿수
            if digit > prev:  # 앞자리가 뒷자리보다 크면 단조아님
                break
            prev = digit
            num //= 10  # 다음 자릿수로 이동
        else:
            total.append(k)

    if total:
        print(f'#{tc}', max(total))
    else:
        print(f'#{tc}', -1)
