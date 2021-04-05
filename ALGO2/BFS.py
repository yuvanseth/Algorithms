import queue
import pdb

def adj_list(graph, file):
    with open(file) as f:
        for line in f:
            vertices = line.split()
            graph[vertices[0]] = vertices[1:]



def BFS(graph, s, d):

    exp = [False] * (len(list(graph.keys())) + 1)
    exp[int(s)] = True

    dist = [0] * (len(list(graph.keys())) + 1)
    
    Q = queue.Queue(maxsize=0)
    Q.put(s)

    while Q.empty() == False:
        v = Q.get()
        for vertex in graph[v]:
            if exp[int(vertex)] == False:
                exp[int(vertex)] == True
                dist[int(vertex)] = dist[int(v)] + 1
                Q.put(vertex)

    print(dist[int(d)])

graph = {}
pdb.set_trace()
adj_list(graph, 'KargerMincut.txt')

BFS(graph, '1', '26')
