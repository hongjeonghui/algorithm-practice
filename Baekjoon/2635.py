N = int(input())

max_len = 0
result = []

for n in range(N + 1):
    seq = [N, n]

    while True:
        next_num = seq[-2] - seq[-1]
        if next_num < 0:
            break
        seq.append(next_num)

    if len(seq) > max_len:
        max_len = len(seq)
        result = seq

print(max_len)
print(*result)
