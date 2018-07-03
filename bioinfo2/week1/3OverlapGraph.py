from fileReader import fileReader

def OverlapGraph(strings):
    adjList = {}
    for string in strings:
        adjList[string] = []

    for item in adjList.keys():
        for string in strings:
            if Suffix(item) == Prefix(string):
                adjList[item].append(string)

    for item in adjList.keys():
        if adjList[item] == []:
            adjList.pop(item)

    return adjList

def Prefix(string):
    return string[:-1]

def Suffix(string):
    return string [1:]

stringList = fileReader()

adjList = OverlapGraph(stringList)

for item in adjList:
    print item + " -> " + ",".join(adjList[item])
