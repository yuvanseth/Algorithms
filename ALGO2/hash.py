import pdb
from collections import defaultdict

hashTable = defaultdict(list)

def hash(i):
    i = abs(i) 
    #pdb.set_trace()
    return i % 1999999

def Insert(hashTable, file):
    with open(file) as f:
        for line in f:
            i = line.split()
            i = int(i[0])
            hashTable[hash(i)].append(i)

def Lookup(hashTable, diff):
    i = hash(diff)
    if diff in hashTable[i]:
        return True
    else:
        return False

def TwoSum(t, hashTable):
    for i in range(1000000):
        for j in range(len(hashTable[i])):  
            #pdb.set_trace() 
            diff = t - hashTable[i][j]
            
            if diff == hashTable[i][j]:
                continue
            if Lookup(hashTable, diff) == True:
                return True
            else:
                continue
    return False

Insert(hashTable, 'hash.txt')

i = -10000
while TwoSum(i, hashTable) == False:
    i += 1

print(TwoSum(i+1, hashTable))


# for i in range(20002):
#     targets = []
#     t = -10000
#     if TwoSum(t, hashTable) == True:
#         targets.append(t)
#     t += 1

# print(len(targets))
