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
            
#arr = [1,2,3,4,5]
#arr = [5,4,3,2,1]
arr = np.random.rand(100000)
quicksort(arr,0, arr.size -1)
#swap(arr, 3, 4)
print(arr)
