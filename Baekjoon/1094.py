x = int(input())
n = [64]

while sum(n) > x:
    smallest = min(n)
    n.remove(smallest)
    half = smallest // 2

    if sum(n) + half >= x:
        n.append(half)
    else:
        n.append(half)
        n.append(half)

print(len(n))
