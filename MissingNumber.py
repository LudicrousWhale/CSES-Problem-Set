n = int(input())
nums = [int(i) for i in input().split()]
e = {}
for i in nums:
    e[i] = 1
for i in range(1, n + 1):
    if i not in e:
        print(i)