import sys

def EulerCycle(adjDict):
    '''
    for key in adjDict.keys():
        path = [key]
        print "performing on seed " + str(key)
        tempDict = deepcopy(adjDict)
        solution = GeneratePath(tempDict, totalEdges, path, key, key)
    '''
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

inputfile = "data.txt"

with open(inputfile, "r") as f:
    data = f.readlines()

cleanData = []

for item in data:
    item = item.replace('\n', '').strip()
    cleanData.append(item)


debruijn = DeBruijn(cleanData)

for item in debruijn:
        adjDict[item.split("->")[0].strip()] = item.split("->")[1].strip().split(",")
        
ans = EulerCycle(adjDict)
print("->".join(map(str,ans)))





