from collections import defaultdict 
import sys

dist = {}
N = 4

class Heap():
    
    def __init__(self, n): 
        self.array = [] 
        self.size = n

    def isEmpty(self): 
        return True if self.size == 0 else False
    
    def heapify(self, i): 

        smallest = i  
        l = 2 * i + 1     
        r = 2 * i + 2      
    
        if l < self.size and self.array[i][1] > self.array[l][1]: 
            smallest = l 
    
        if r < self.size and self.array[smallest][1] > self.array[r][1]: 
            smallest = r 
    
        if smallest != i: 
            self.array[i],self.array[smallest] = self.array[smallest],self.array[i] 
    
            self.heapify(smallest)

    def extractMin(self): 
  
        if self.isEmpty() == True: 
            return

        self.array[0], self.array[self.size-1] = self.array[self.size-1], self.array[0]

        root = self.array.pop(self.size-1)
        self.size -= 1
        self.heapify(0)

        return root

class Graph():
    def __init__(self, N):
        self.size = N
        self.graph = defaultdict(list)

    def adj_list(self, file):
        with open(file) as f:
            for line in f:
                vertices = line.split()
                for vertex in vertices[1:]:
                    self.graph[int(vertices[0])].append([int(i) for i in vertex.split(',')])
     
    def Dijkstra(self, s):
        global dist

        minHeap = Heap(self.size)
            
        for v in range(1, self.size+1):    
            minHeap.array.append([v, sys.maxsize])
            

        dist[s] = 0
        minHeap.array[s-1][1] = 0
        minHeap.heapify(0)
        

        while minHeap.isEmpty() == False:
            minNode = minHeap.extractMin()
            dist[minNode[0]] = minNode[1]
            w = minNode[0]

            for vertex in self.graph[w]:
                v = vertex[0]
                key = minHeap.array[v-1][1] 
                min(key, dist[w] + vertex[1])
                minHeap.heapify(0)

    
graph = Graph(4)
graph.adj_list('test.txt')   
graph.Dijkstra(1)
print(dist) 
