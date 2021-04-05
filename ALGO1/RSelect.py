import random
import sys
sys.setrecursionlimit(10000)

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

def RSelect(arr, start, end, i):
    if start ==  end:
        return arr[1]
    pivot = choosePivot(arr, start, end)
    pIndex = partition(arr, start, end, pivot)
    if pIndex == i:
        return arr[pIndex]
    if pIndex > i:
        return RSelect(arr, 0, pIndex-1, i)
    if pIndex < i:
        return RSelect(arr, pIndex+1, end, i-pIndex)
        

if __name__ == "__main__": 
    array = [3456, -123984, 786, -46, 7725, 18, 0]
    j = RSelect(array, 0, len(array) - 1, 3)
    print(j)
    

    