N = int(input())
for tc in range(N):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a = A[1:]
    b = B[1:]

    Acnt_4 = Acnt_3 = Acnt_2 = Acnt_1 = 0
    for i in a:
        if i == 4: Acnt_4 += 1
        elif i == 3: Acnt_3 += 1
        elif i == 2: Acnt_2 += 1
        elif i == 1: Acnt_1 += 1

    Bcnt_4 = Bcnt_3 = Bcnt_2 = Bcnt_1 = 0
    for j in b:
        if j == 4: Bcnt_4 += 1
        elif j == 3: Bcnt_3 += 1
        elif j == 2: Bcnt_2 += 1
        elif j == 1: Bcnt_1 += 1

    if Acnt_4 != Bcnt_4:
        print('A' if Acnt_4 > Bcnt_4 else 'B')
    elif Acnt_3 != Bcnt_3:
        print('A' if Acnt_3 > Bcnt_3 else 'B')
    elif Acnt_2 != Bcnt_2:
        print('A' if Acnt_2 > Bcnt_2 else 'B')
    elif Acnt_1 != Bcnt_1:
        print('A' if Acnt_1 > Bcnt_1 else 'B')
    else:
        print('D')
