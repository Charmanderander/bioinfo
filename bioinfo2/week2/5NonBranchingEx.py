import sys

def MaximalNonBranchingPaths(adjDict, inCount, outCount):
    paths = []
   
    for node in list(adjDict.keys()):
        # if node is not a 1-in-1-out
        if inCount[node] != 1 or outCount[node] != 1:
            if outCount[node] > 0:
                for outNode in adjDict[node]:
                    present = 0
                    nonBranchingPath = []
                    nonBranchingPath.append(node)
                    nonBranchingPath.append(outNode)
                    while inCount[outNode] == 1 and outCount[outNode] == 1:
                        nextNode = adjDict[outNode][0]
                        if nextNode == node:
                            break 
                        nonBranchingPath.append(nextNode)
                        outNode = nextNode

                    for path in paths:
                        if sorted(nonBranchingPath) == sorted(path):
                            present = 1
                    if not present:
                        paths.append(nonBranchingPath)
    
        # handling isolated cycles
        if inCount[node] == 1 and outCount[node] == 1:
            for outNode in adjDict[node]:
                present = 0
                nonBranchingPath = []
                nonBranchingPath.append(node)
                nonBranchingPath.append(outNode)
                while inCount[outNode] == 1 and outCount[outNode] == 1:
                    nextNode = adjDict[outNode][0]
                    nonBranchingPath.append(nextNode)
                    if nextNode == node:
                        for path in paths:
                            if sorted(nonBranchingPath[1:]) == sorted(path[1:]):
                                present = 1
                        if not present:
                            paths.append(nonBranchingPath)
                        break
                    outNode = nextNode

        
    return paths
           

def FindInOutCount(adjDict):
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
        
    return inCount, outCount

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

def rotate(l, n):
    return l[n:] + l[:n]

adjDict = {}
'''
data = sys.stdin.read().split('\n')
'''

with open("data.txt", "r") as f:
    data = f.readlines()

cleanData = []

for item in data:
    item = item.replace('\n', '').strip()
    cleanData.append(item)

adjData = cleanData

#adjData = DeBruijn(cleanData)

for item in adjData:
        adjDict[item.split("->")[0].strip()] = item.split("->")[1].strip().split(",")

inCount, outCount = FindInOutCount(adjDict)
'''
print adjDict
'''
paths = MaximalNonBranchingPaths(adjDict, inCount, outCount)
for path in paths:
    print(" -> ".join(path))
