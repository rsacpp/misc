import numpy as np


def swap(arr, a, b):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]


result = []


def heapsort(arr):
    size = len(arr)
    for _ in range(0, size):
        for index in range(int(size/2), -1, -1):
            size = len(arr)
            if size == 0:
                return
            if size == 1:
                result.append(arr.pop())
                return
            leftchild = (index+1) * 2 - 1
            rightchild = (index+1) * 2
            if leftchild <= size - 1 and arr[index] > arr[leftchild]:
                swap(arr, index, leftchild)
            if rightchild <= size - 1 and arr[index] > arr[rightchild]:
                swap(arr, index, rightchild)
        result.append(arr.pop(0))


arr = list(np.random.rand(10000))
heapsort(arr)
print(result)
