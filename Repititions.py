string = input()
maxLength = 1
currentLength = 1
for idx in range(1, len(string)):
    if string[idx - 1] == string[idx]:
        currentLength += 1
    else:
        currentLength = 1
    if currentLength > maxLength:
        maxLength = currentLength
print(maxLength)
