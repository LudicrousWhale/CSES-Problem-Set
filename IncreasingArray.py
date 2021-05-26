n = int(input())
array = [int(i) for i in input().split()]

ans = 0
for i in range(1, n):
    if array[i - 1] > array[i]:
        ans += (array[i - 1] - array[i])
        array[i] = array[i - 1]

print(ans)

