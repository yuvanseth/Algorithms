import random
import pdb
import sys

#sys.setrecursionlimit(10**4) 

numbers = [i for i in range(0,100)]
random.shuffle(numbers)

maxHeap = []
minHeap = []
minHeap.append(numbers[0])
maxHeap.append(numbers[1])


def parent(k):
    if k%2 == 0:
        return (k/2)-1
    else:
        return int(k/2)

def leftChild(k):
    return 2*k + 1

def rightChild(k):
    return 2*k + 2

def insertMinheap(minHeap, i):
    minHeap.append(i)
    k = minHeap.index(i)

    while parent(k) >= 0 and minHeap[k] < minHeap[parent(k)]:
        minHeap[k], minHeap[parent(k)] = minHeap[parent(k)], minHeap[k]
        k = parent(k)

def insertMaxheap(maxHeap, i):
    maxHeap.append(i)
    k = maxHeap.index(i)
    #pdb.set_trace()
    while parent(k) >= 0 and maxHeap[k] > maxHeap[parent(k)]:
        maxHeap[k], maxHeap[parent(k)] = maxHeap[parent(k)], maxHeap[k]
        k = parent(k)

def extractMin(minHeap):
    n = len(minHeap)
    minHeap[0], minHeap[n-1] = minHeap[n-1], minHeap[0]
    minimum = minHeap.pop()
    n -= 1
    def minHeapifydown(minHeap, size, k):
        smallest = k
        l = leftChild(k)
        r = rightChild(k) 
        
        #pdb.set_trace()
        if l < size and minHeap[k] > minHeap[l]:
            smallest = l
        
        if r < size and minHeap[smallest] > minHeap[r]:
            smallest = r
        
        if smallest != maxHeap[k]:
            minHeap[k],minHeap[smallest] = minHeap[smallest],minHeap[k]
            minHeapifydown(minHeap, size, smallest)   
        
    minHeapifydown(minHeap, n, 0)
    return minimum

def extractMax(maxHeap):
    n = len(maxHeap)
    maxHeap[0], maxHeap[n-1] = maxHeap[n-1], maxHeap[0]
    maximum = maxHeap.pop()
    n -= 1
    def minHeapifydown(maxHeap, size, k):
        largest = k
        l = leftChild(k)
        r = rightChild(k) 
        
        #pdb.set_trace()
        if l < size and maxHeap[k] < maxHeap[l]:
            largest = l
        
        if r < size and maxHeap[largest] < maxHeap[r]:
            largest = r
        
        if largest != maxHeap[k]:
            maxHeap[k],maxHeap[largest] = maxHeap[largest],maxHeap[k]
            minHeapifydown(maxHeap, size, largest)   
        
    minHeapifydown(maxHeap, n, 0)
    return maximum


def Medians(i):
    if i < maxHeap[0]:
        insertMaxheap(maxHeap, i)
        if len(maxHeap) >= len(minHeap):
            maximum = extractMax(maxHeap)
            insertMinheap(minHeap, maximum)

    else:
        insertMinheap(minHeap, i)
        if len(minHeap) >= len(maxHeap) + 1:
            minimum = extractMin(minHeap)
            insertMaxheap(maxHeap, minimum)

    if len(maxHeap) != len(minHeap):
        return minHeap[0]
    else:
        return maxHeap[0]
    
medians = []
for i in numbers[2:]:
    medians.append(Medians(i))

print(medians)
