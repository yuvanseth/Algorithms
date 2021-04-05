import random
import sys
sys.setrecursionlimit(10000)

def mergeSort(arr):
    
    if len(arr) > 1:
        mid = len(arr) // 2
        l = arr[:mid]
        r = arr[mid:]

        mergeSort(l)
        mergeSort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i+=1
            else:
                arr[k] = r[j]
                j+=1
            k+=1
        
        while i < len(l):
            arr[k] = l[i]
            i+=1
            k+=1
        
        while j < len(r):
            arr[k] = r[j]
            j+=1
            k+=1

def choosePivot(arr, start, end):
    count = 0
    temp = []
    medians = []
    for j in range(0,len(arr)):
        if count == 5:
            mergeSort(temp)
            medians.append(temp[int((len(temp)+1)/2)])
            count = 0
            temp.clear()
        temp.append(arr[j])
        count += 1
    
    if start == end:
        return medians[0]
    choosePivot(medians, 0, len(medians))
    

        
            
    
def partition(arr, start, end, pivot):    
    arr[start], arr[pivot] = arr[pivot], arr[start]
    sep = start+1
    for i in range(start+1, end+1):
        if arr[i] < arr[start]:
            arr[i], arr[sep] = arr[sep], arr[i]
            sep += 1
    arr[start], arr[sep-1] = arr[sep-1], arr[start]
    return sep-1

def DSelect(arr, start, end, i):
    if start ==  end:
        return arr[1]
    pivot = choosePivot(arr, start, end)
    pIndex = partition(arr, start, end, pivot)
    if pIndex == i:
        return arr[pIndex]
    if pIndex > i:
        return DSelect(arr, 0, pIndex-1, i)
    if pIndex < i:
        return DSelect(arr, pIndex+1, end, i-pIndex)
        

if __name__ == "__main__": 
    array = [3456, -123984, 786, -46, 7725, 18]
    j = DSelect(array, 0, len(array) - 1, 3)
    print(j)