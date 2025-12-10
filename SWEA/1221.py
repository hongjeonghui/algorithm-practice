T = int(input())
for tc in range(1, T+1):
    _, N = input().split()
    N = int(N)
    arr = (input().split())

    nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    arr.sort(key=lambda x: nums.index(x))

    print(f'#{tc}')
    print(*arr)
