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

        if prefixString in pairDict:
            pairDict[prefixString].append(suffixString)
        else:
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

    # closing the loop
    if unbalancedIn != "" and unbalancedOut != "":
        adjDict[unbalancedIn] = [unbalancedOut]

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

def StringSpelledByGappedPatterns(gappedPatterns, k, d):
    firstPatterns = []
    secondPatterns = []

    print(gappedPatterns)

    for item in gappedPatterns:
        firstPatterns.append(item[:k-1])
        secondPatterns.append(item[-k+1:])

    print(firstPatterns)
    print(secondPatterns)

    prefixString = StringSpelledByPatterns(firstPatterns, k)
    suffixString = StringSpelledByPatterns(secondPatterns, k)

    print(prefixString)
    print(suffixString)

    for x in range(k + d + 1, len(prefixString)):
        if prefixString[x] != suffixString[x - k - d]:
            return "no string spelled"

    return prefixString + suffixString[-(k + d):]

def StringSpelledByPatterns(patterns, k):
    string = ""
    lastPattern = patterns[-1]
    patterns.pop(-1)
    for pattern in patterns:
        string += pattern[0]
    string += lastPattern
    return string

inputfile = "data.txt"

with open(inputfile, "r") as f:
    data = f.readlines()

params = data[0].split(" ")

k = int(params[0].strip().replace('\n', ''))
d = int(params[1].strip().replace('\n', ''))

data.pop(0)

dataList = []

for item in data:
    cleanString = item.strip().replace('\n', '')
    dataList.append(cleanString)

adjDict = GeneratePairDict(dataList)

newAdjDict, unbalancedOut = FindUnbalancedNode(adjDict)

ans = EulerPath(newAdjDict)

ans.pop(0)
#rotate the list to bring the unbalanced node to the head
rotated = rotate(ans, ans.index(unbalancedOut))

ansStr = StringSpelledByGappedPatterns(rotated, k, d)

print(ansStr)
