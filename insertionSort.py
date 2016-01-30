import random

def insertionSort(numArray):
    for j in range(1,len(numArray)):
        key = numArray[j]
        i = j-1
        while i>-1 and numArray[i] > key:
            numArray[i+1] = numArray[i]
            i = i-1
        numArray[i+1] = key
    return numArray

def generateNumArray():
    numArray = []
    for i in range(0,100):
        num = random.randint(0,1000)
        numArray.append(num)

    return numArray


nums = generateNumArray()

print(nums)
print(insertionSort(nums))
