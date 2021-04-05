from collections import defaultdict
import pdb

# adjacency list(dict)
graph = []
leader = [None] * 501
sub = defaultdict(list)

with open('cluster.txt') as file:
    # going line-by-line in file
    #pdb.set_trace()
    
    for line in file.readlines()[1:]:
        v = line.split()
        # convert str to int
        for i in range(3):
            v[i] = int(v[i])

        graph.append(v)
        leader[v[0]] = v[0]
        if len(sub[v[0]]) == 0:
            sub[v[0]].append(v[0])

graph.sort(key=lambda x: x[2])

k = 500
leader[k] = k
sub[k].append(k)




for i in graph:
    if k > 4:
        if leader[i[0]] != leader[i[1]]:
            if len(sub[i[0]]) >= len(sub[i[1]]):
                for j in sub[i[1]]:
                    leader[j] = i[0]
                    sub[i[1]].pop(0)
                    sub[i[0]].append(j)
            else:
                for j in sub[i[0]]:
                    leader[j] = i[1]
                    sub[i[0]].pop(0)
                    sub[i[1]].append(j)
            
            k -= 1
        else:
            continue

  

for i in graph:
    if leader[i[0]] != leader[i[1]]:
        print(i[2])
        break
    else:
        continue

no



 
