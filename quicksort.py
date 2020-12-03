import numpy as np

def swap(arr, a , b):
    if a == b:
        return
    arr[a], arr[b] = arr[b], arr[a]

def quicksort(arr, left, right):
    if left >= right:
        return
    leftpos, rightpos = left, right-1
    thevalue = arr[right]
    while leftpos < right:
        while arr[leftpos] < thevalue:
            leftpos += 1
            if leftpos == right:
                break
        while arr[rightpos] > thevalue:
            rightpos -= 1
            if rightpos == left:
                break
        if leftpos < rightpos:
            swap(arr, leftpos, rightpos)
        else:
            arr[right] = arr[leftpos]
            arr[leftpos] = thevalue
            quicksort(arr, left, rightpos)
            quicksort(arr, leftpos, right)
            break

def quicksort2(arr, left, right):
    if left >= right:
        return
    if left + 1 == right:
        if arr[left] > arr[right]:
            swap(arr, left, right)
        return
    leftpos, rightpos = left, right-1
    thevalue = arr.pop(right)
    while leftpos < right:
        while arr[leftpos] < thevalue:
            leftpos += 1
            if leftpos == right:
                break
        while arr[rightpos] > thevalue:
            rightpos -= 1
            if rightpos == left:
                break
        if leftpos < rightpos:
            swap(arr, leftpos, rightpos)
        else:
            arr.insert(leftpos, thevalue)
            quicksort2(arr, left, rightpos)
            quicksort2(arr, leftpos, right)
            break
#arr = [1,2,3,4,5]
#arr = [5,4,3,2,1]
arr = np.random.rand(100)
quicksort(arr,0, arr.size -1)
print(arr)

arr2 = np.random.rand(100)
#arr2 = range(6,1, -1)
arr2 = list(arr2)
quicksort2(arr2 ,0, len(arr2) -1)
print(arr2)
