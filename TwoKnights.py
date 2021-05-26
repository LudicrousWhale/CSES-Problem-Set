n = int(input())

for k in range(1, n + 1):
    a1 = k * k
    a2 = a1 * ((a1 - 1) // 2)
    if k > 2:
        a1 -= 4 * (k - 1) * (k - 2)
    print(a2)