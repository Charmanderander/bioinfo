def EulerPath(adjDict):
    path = []
    stack = []
    reversedPath = GeneratePath(adjDict,path, stack)
    path = reversedPath[::-1]

    return path

def GeneratePairDict(dataset):
    ''' Each dataset has a pair of strings
    We generate a dictionary whose key is a list of prefixs
    the prefix key will point to the suffix values
    '''

    pairDict = {}

    for item in dataset:
        pairs = item.split('|')
        prefixString = ""
        suffixString = ""

        for string in pairs:
            prefixString += Prefix(string)
            suffixString += Suffix(string)
        
        pairDict[prefixString] = [suffixString]

    return pairDict

def FindUnbalancedNode(adjDict):
    # We modify the list and close the loop
    outCount = {}
    inCount = {}

    keys = adjDict.keys()

    possibleNodes = []

    for key in keys:
        possibleNodes += [item for item in adjDict[key]]

    possibleNodes = possibleNodes + list(set(keys) - set(possibleNodes))

    unbalancedIn = unbalancedOut = ""

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

    print(inCount)
    print(outCount)

    # closing the loop
    if unbalancedIn != "" and unbalancedOut != "":
        if unbalancedIn!=unbalancedOut:
            adjDict[unbalancedIn].append(unbalancedOut)
    else:
        unbalancedIn = 0
        unbalancedOut = 0

    return adjDict, unbalancedOut


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

def Prefix(string):
    return string[:-1]

def Suffix(string):
    return string [1:]

def rotate(l, n):
    return l[n:] + l[:n]

with open("data.txt", "r") as f:
    data = f.readlines()

k = 3 
d = 1

dataList = []

for item in data:
    cleanString = item.strip().replace('\n', '')
    dataList.append(cleanString)

adjDict = GeneratePairDict(dataList)
print(adjDict)
newAdjDict, unbalancedOut = FindUnbalancedNode(adjDict)
print("###")
print(newAdjDict)
ans = EulerPath(newAdjDict)

ans.pop(0)
#rotate the list to bring the unbalanced node to the head
rotated = rotate(ans, ans.index(unbalancedOut))

print(rotated)

ansStr = rotated[0][:k-1]

rotated.pop(0)

for item in rotated:
    print(item)
    ansStr += item[k-2]

ansStr += rotated[-k][k-1:]

for item in rotated[-(k-1):]:
    ansStr += item[-1]

print(ansStr)
