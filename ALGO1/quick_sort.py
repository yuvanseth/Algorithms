import random
import sys
sys.setrecursionlimit(10000)
count = 0

def choosePivot(arr, start, end):
    pivot = random.randint(start, end)
    return pivot

def partition(arr, start, end, pivot):    
    arr[start], arr[pivot] = arr[pivot], arr[start]
    sep = start+1
    for i in range(start+1, end+1):
        if arr[i] < arr[start]:
            arr[i], arr[sep] = arr[sep], arr[i]
            sep += 1
    arr[start], arr[sep-1] = arr[sep-1], arr[start]
    return sep-1

def quicksort(arr, start, end):
    if start < end:
        global count
        count = count + len(arr) - 1
        pivot = choosePivot(arr, start, end)
        pIndex = partition(arr, start, end, pivot)
        quicksort(arr, start, pIndex-1)
        quicksort(arr, pIndex+1, end)

if __name__ == "__main__": 
    f = open('quicksort.txt', 'r')
    array = []
    for line in f.readlines():
        array.append(int(line))
    quicksort(array, 0, len(array) - 1)
    print(count)
    

    