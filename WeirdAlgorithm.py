n = int(input())
output = []
output.append(str(n))
while n != 1:
    if n % 2 == 0:
        n = n // 2
        output.append(str(n))
    else:
        n = int(n * 3 + 1)
        output.append(str(n))

print(' '.join(output))