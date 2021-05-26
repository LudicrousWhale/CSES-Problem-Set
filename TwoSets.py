# arr is the data recieved,
# nr is the number of redundant bits
def detectPositionOfError(arr, nr):
    n = len(arr)
    res = 0

    for i in range(nr):
        val = 0
        for j in range(1, n + 1):
            if(j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])

        res = res + val*(10**i)
    return int(str(res), 2)

# nr required for the above function is calculated 
# with the function calculateRedundantBits(m) function below
def calculateRedundantBits(m):
    for i in range(m):
        if(2**i >= m + i + 1):
            return i


origDataLen = int(input("Enter the length of the data (between 7 and 31): "))
numOfRedundantBits = calculateRedundantBits(origDataLen)



if origDataLen < 7 or origDataLen > 31:
    print("Incorrect value, please enter the value again.")
    
else:
    data = input("Enter the data (between 7 and 31): ")
    lenOfRecievedData = len(data)
    if lenOfRecievedData - numOfRedundantBits != origDataLen:
        print("Incorrect value, please enter the value again.")
    else:
        positionOfError = detectPositionOfError(data, numOfRedundantBits)

        if positionOfError == 0:
            print("Data Received Correctly: YES")
            print("Bit position containing Error (mention position): NA")
        else:
            print("Data Received Correctly: NO")
            print("Bit position containing Error (mention position):" + str(positionOfError))
            if data[positionOfError] == '0':
                copy = data[:positionOfError] + '1' + data[positionOfError + 1:]
            elif data[positionOfError] == '1':
                copy = data[:positionOfError] + '0' + data[positionOfError + 1:]
            print("Correct data is: ", copy)
                



