from collections import defaultdict

class Graph:
    
    def __init__(self, n):
        self.g = defaultdict(list)
        self.size = n
    
    def addEdge(self,x,y):
        self.g[x].append(y)

    def DFS(self, s, exp, order):
        exp[s] = True
        for vertex in self.g[s]:
            if exp[vertex] == False:
                self.DFS(vertex, exp, order)
        order.insert(0,s)

    def DFSloop(self):
        exp = [False] * (self.size + 1)
        order = []
        
        for i in range(1,(self.size + 1)):
            if exp[i] == False:
                self.DFS(i, exp, order) 
        
        print(order)

graph = Graph(4)

graph.addEdge(1,2)
graph.addEdge(1,3)
graph.addEdge(2,4)
graph.addEdge(3,4)

graph.DFSloop()



