import sys
import math

def EulerCycle(adjDict):
    path = []
    stack = []
    reversedPath = GeneratePath(adjDict,path, stack)
    path = reversedPath[::-1]
    
    return path
    

def GeneratePath(adjDict, path, stack):
    dst = list(adjDict.keys())[0]
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

def binaryGen(n):
    ceiling = 0
    binaryArr = []

    for x in range(n):
        ceiling += int(math.pow(2,x))

    for i in range(ceiling+1):
        b = bin(i)[2:]
        l = len(b)
        b = str(0) * (n - l) + b
        binaryArr.append(b)

    return binaryArr

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


adjDict = {}
#data = sys.stdin.read().split('\n')

n = 6 

BinaryData = binaryGen(n)

data = DeBruijn(BinaryData)

for item in data:
        adjDict[item.split("->")[0].strip()] = list(item.split("->")[1].strip().split(","))

ans = EulerCycle(adjDict)

ansStr = ans[0]

ans.pop(0)

for string in ans:
   ansStr += string[-1]

print (ansStr[:-(n-1)])



