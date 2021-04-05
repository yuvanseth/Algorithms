from collections import defaultdict
import csv
import sys

sys.setrecursionlimit(100000)
N = 875714
# array storing finishing times of the respective indices
t = [0] * (N+1) 
# counting how many time nodes originate from leader/source node
count = [0] * (N+1)

class Graph:
    
    def __init__(self, n):
        # dict storing graph as adj list
        self.graph = defaultdict(list)
        # dict with keys swapped with their finishing times
        self.graph_time = defaultdict(list)
        # dict with values too swapped with their finishing times
        self.graph_t = defaultdict(list)
        self.size = n

    # function to store graph in reverse as adj list 
    def adj_list_rev(self, file):
        # converted txt to csv file so as to get rid of '' from numbers, set delimiter as space
        with open(file) as f:
            reader = csv.reader(f, delimiter=" ", skipinitialspace=True)
            # loop to store graph as reverse
            for line in reader:
                vertices = [i for i in line]
                # each line showing unexpected '' on the 3rd index, so delete
                del vertices[2]
                vertices = [int(i) for i in vertices]
                self.graph[vertices[1]].append(vertices[0])
    
    # function to store graph as adj list
    def adj_list(self, file):
        with open(file) as f:
            reader = csv.reader(f, delimiter=" ", skipinitialspace=True)
            # loop to store graph
            for line in reader:
                vertices = [i for i in line]
                # each line showing unexpected '' on the 3rd index, so delete
                del vertices[2]
                vertices = [int(i) for i in line]
                self.graph[vertices[0]].append(vertices[1])
            # loop to store graph by replacing keys with their finising times
            for i in range(1, self.size+1):
                self.graph_t[t[i]] = self.graph[i]
            # loop to store graph by replacing values with their finising times
            for i in range(1, 10):
                for j in range(len(self.graph_t[i])):
                    self.graph_time[i].append(t[self.graph_t[i][j]])

    # 1st pass DFS  
    def DFS1(self, s, exp):
        exp[s] = True
        
        for vertex in self.graph[s]:
            if exp[vertex] == False:
                self.DFS1(vertex, exp)
        # store the node's finishing time after no more edges left unexplored
        global t
        t[0] += 1
        t[s] = t[0]
       
    # 1st pass DFS outer loop
    def DFSloop1(self):
        # create local array to store explored state of node
        exp = [False] * (self.size + 1)
        for i in range(self.size, 0, -1):
            if exp[i] == False:
                self.DFS1(i, exp) 

    # 2nd pass DFS
    def DFS2(self, s, exp, leader):
        exp[s] = True
        global count
        # increase count of nodes for a leader/source node
        count[leader] += 1
        for vertex in self.graph_time[s]:
            if exp[vertex] == False:
                self.DFS2(vertex, exp, leader)

    # 2nd pass DFS loop
    def DFSloop2(self):
        exp = [False] * (self.size + 1)
        global count
        for i in range(self.size, 0, -1):
            if exp[i] == False:
                leader = i
                self.DFS2(i, exp, leader)



graph = Graph(N)
graphr = Graph(N)
graphr.adj_list_rev('SCC.csv')
graphr.DFSloop1()
graph.adj_list('SCC.csv')
graph.DFSloop2()

count.sort(reverse=True)
print(count[:5])

