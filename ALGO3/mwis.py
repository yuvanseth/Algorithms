import pdb

arr = [None]*1001
arr[0] = 0
v = []

with open('mwis.txt') as file:
    lines = file.readlines()
    lines[1] = int(lines[1].rstrip())
    arr[1] = lines[1]
    for i in range(2, 1001):
        lines[i] = int(lines[i].rstrip())
        arr[i] = max(arr[i-1], arr[i-2]+lines[i])
        
i = 1000
while i>=1:
    if arr[i-1] >= arr[i-2]+lines[i]:
        i -= 1
    else:
        v.append(i)
        i -= 2
print(len(arr))
print(v)



