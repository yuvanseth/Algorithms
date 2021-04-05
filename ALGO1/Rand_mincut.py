import random

def adj_list(graph, file):
    with open(file) as f:
        for line in f:
            line.strip()
            vertices = line.split()
            graph[vertices[0]] = vertices[1:]

def randVertices(graph):
    u = random.choice(list(graph.keys()))
    v = random.choice(graph[u])
    return (u, v)

def Karger(graph):
    while len(graph) > 2:
        (u, v) = randVertices(graph)
        graph[u].extend(graph[v])
        
        for vertex in graph[v]:
            graph[vertex].remove(v)
            graph[vertex].append(u)
        
        graph[u] = list(filter(lambda x: x != u, graph[u]))

        del graph[v]
    
    length = [len(graph[key]) for key in graph.keys()]
    return length[0]

graph = {}
adj_list(graph, 'KargerMincut.txt')

mincut = Karger(graph)
print(mincut)