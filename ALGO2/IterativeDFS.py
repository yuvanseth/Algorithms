from collections import defaultdict

class Graph:
    
    def __init__(self, n):
        self.g = defaultdict(list)
        self.size = n
    
    def addEdge(self,x,y):
        self.g[x].append(y)

    def DFS(self, s, exp):
        exp[s] = True
        stack = []
        stack.append(s)
        while(len(stack) > 0):
            v = stack.pop()
            print(v)
            for vertex in self.g[v]:
                if exp[vertex] == False:
                    exp[vertex] = True
                    stack.append(vertex)
            

    def DFSloop(self):
        exp = [False] * (self.size + 1)
        
        for i in range(1,(self.size + 1)):
            if exp[i] == False:
                self.DFS(i, exp) 
        
        

graph = Graph(4)

graph.addEdge(1,2)
graph.addEdge(1,3)
graph.addEdge(2,4)
graph.addEdge(3,4)

graph.DFSloop()



