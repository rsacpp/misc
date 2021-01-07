import random

def swap(arr, indexA, indexB):
    if indexA == indexB:
        return
    if arr[indexA] == arr[indexB]:
        return
    arr[indexA], arr[indexB] = arr[indexB], arr[indexA]

def sort(arr, fromIndex, toIndex):
    if fromIndex >= toIndex:
        return
    if fromIndex + 1 == toIndex:
        if arr[fromIndex] > arr[toIndex]:
            swap(arr, fromIndex, toIndex)
        return
    threshold = arr[fromIndex]
    headIndex = fromIndex + 1
    tailIndex = toIndex
    while headIndex < tailIndex:
        while headIndex < tailIndex:
            if arr[headIndex] >= threshold:
                break
            else:
                headIndex+=1
        if headIndex == tailIndex:
            break
        while headIndex < tailIndex:
            if arr[tailIndex] < threshold:
                break
            else:
                tailIndex-=1
        if headIndex == tailIndex:
            break
        if headIndex < tailIndex:
            arr[headIndex] , arr[tailIndex] = arr[tailIndex], arr[headIndex]
            headIndex+=1
            tailIndex-=1
        if headIndex > tailIndex:
            pass
    # 3, [1,2,1,0]
    if arr[headIndex] < threshold:
        swap(arr, fromIndex, headIndex)
        sort(arr, fromIndex, headIndex - 1)
        sort(arr, headIndex, toIndex)
    # 3, [1, 2, 1,3]
    if arr[headIndex] >= threshold:
        swap(arr, fromIndex, headIndex -1)
        sort(arr, fromIndex, headIndex -1)
        sort(arr, headIndex, toIndex)

arr = []

n = 999
rangeFrom = 1
rangeTo = 0x123
for _ in range(0, n):
    arr.append(random.randint(rangeFrom, rangeTo))
print(arr)
sort(arr, 0, n-1)
print(arr)
