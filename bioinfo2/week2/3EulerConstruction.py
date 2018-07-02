import sys
import math

def EulerCycle(adjDict):
    path = []
    stack = []
    reversedPath = GeneratePath(adjDict,path, stack)
    path = reversedPath[::-1]
    
    return path
    
def FindUnbalancedNode(adjDict):
    # We modify the list and close the loop
    outCount = {}
    inCount = {}

    keys = adjDict.keys()

    possibleNodes = []
    
    for key in keys:
        possibleNodes += [item for item in adjDict[key]]

    possibleNodes = possibleNodes + list(set(keys) - set(possibleNodes)) 

    unbalancedIn = unbalancedOut = 0

    for key1 in possibleNodes:
        if key1 in keys:
            outCount[key1] = len(adjDict[key1])
        else:
            outCount[key1] = 0
        inCount[key1] = 0
        for key2 in keys:
            inCount[key1] += adjDict[key2].count(key1)
        
        if outCount[key1] > inCount[key1]:
            unbalancedOut = key1
        if outCount[key1] < inCount[key1]:
            unbalancedIn = key1

    # closing the loop
    if unbalancedIn != 0 and unbalancedOut != 0:
        adjDict[unbalancedIn] = [unbalancedOut]

    return adjDict, unbalancedOut

def GeneratePath(adjDict, path, stack):
    dst = adjDict.keys()[0]
    while True:
        if len(list(adjDict[dst])) == 0:
            # If current vertex has no out-going edges (i.e. neighbors)
            # add it to circuit
            path.append(dst)      
            if stack == []:
                break
            # set last vertex from the stack as the current one
            dst = stack[-1]
            # remove the last vertex from the stack
            stack.pop()
   
        else:
            # Otherwise (in case it has out-going edges, i.e. neighbors)
            # add the vertex to the stack
            stack.append(dst)
            # take any of its neighbors, set that neighbor as the current vertex
            newdst = adjDict[dst][0]
            # remove the edge between that vertex and selected neighbor
            adjDict[dst].pop(0)
            dst = newdst
       

    return path

def rotate(l, n):
    return l[n:] + l[:n]

def DeBruijn(strings):
    presufDict = {}

    for string in strings:
        presufDict[Prefix(string)] = []

    for string in strings:
        presufDict[Prefix(string)].append(Suffix(string))

    adjMatrix = []

    for item in presufDict:
        adjMatrix.append(item + " -> " + ",".join(presufDict[item]))

    return adjMatrix

def Prefix(string):
    return string[:-1]

def Suffix(string):
    return string [1:]

def binaryGen(n):
    ceiling = 0
    binaryArr = []

    for x in range(n):
        ceiling += int(math.pow(2,x))

    for i in xrange(ceiling+1):
        b = bin(i)[2:]
        l = len(b)
        b = str(0) * (n - l) + b
        binaryArr.append(b)

    return binaryArr

adjDict = {}
cleanStrings = []

'''
with open("data.txt", "r") as f:
    data = f.readlines()
'''

data = binaryGen(5)

for string in data:
    cleanStrings.append(string.replace("\n","").strip())

adjMatrix = DeBruijn(cleanStrings)

'''
data = sys.stdin.read().split('\n')
'''

for item in adjMatrix:
        adjDict[item.split("->")[0].strip()] = list(item.split("->")[1].strip().split(","))

adjDict, unbalancedOut = FindUnbalancedNode(adjDict)

ans = EulerCycle(adjDict)
ans.pop()

#rotate the list to bring the unbalanced node to the head
rotated = rotate(ans, ans.index(unbalancedOut))

finalStr = rotated[0]

rotated.pop()

for item in rotated:
    finalStr += item[-1]

print(finalStr)



