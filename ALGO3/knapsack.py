from collections import defaultdict
import pdb

stones = defaultdict(list)
stones[1] = [1,1]
stones[2] = [3,4]
stones[3] = [4,5]
stones[4] = [5,7]

arr = [[None for i in range(8)] for j in range(5)]

w = 7


for x in range(8):
    arr[0][x] = 0 

for i in range (1,5):
    for j in range (1,8):
        if stones[i][1] >= j:
            arr[i][j] = arr[i-1][j]
        else:
            arr[i][j] = max(arr[i-1][j], arr[i-1][j - stones[i][1]] + stones[i][0])

print(arr)

i=4
j=7

while i>0 and j>0:
    #pdb.set_trace()
    if stones[i][1] >= j or arr[i-1][j] > arr[i-1][j - stones[i][1]] + stones[i][0]:
        print(stones[i-1][0])
        i -= 1

    else:
        print(stones[i][0])
        j = j - stones[i][1]
        i -= 1
        