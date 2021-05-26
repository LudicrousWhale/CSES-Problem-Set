"""
1, 0 = 1
0, 1 = 2
1, 1 = 3
1, 0 = 4
2, 0 = 5
2, 1 = 6
2, 2 = 7
1, 3 = 8
"""

n = int(input())
yx = [[int(i) for i in input().split()] for j in range(n)]
for test in range(n):
    s = yx[test]
    y = s[0]
    x = s[1]
    z = max(y, x)
    ans = 0
    z2 = (z - 1)*(z - 1)
    if z % 2 == 0:
        if y == z:
            ans = z2 + x
        else:
            ans = z2 + 2 * z - y
    else:
        if x == z:
            ans = z2 + y
        else:
            ans = z2 + 2 * z - x

    print(ans)

