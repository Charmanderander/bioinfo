import sys

def EulerCycle(adjDict):
    path = []
    stack = []
    reversedPath = GeneratePath(adjDict,path, stack, 2)
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

def GeneratePath(adjDict, path, stack, dst):
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

adjDict = {}
'''
data = sys.stdin.read().split('\n')
'''

with open("data.txt", "r") as f:
    data = f.readlines()

for item in data:
        adjDict[int(item.split("->")[0])] = list(map(int,item.split("->")[1].strip().split(",")))

adjDict, unbalancedOut = FindUnbalancedNode(adjDict)

ans = EulerCycle(adjDict)
ans.pop(0)
#rotate the list to bring the unbalanced node to the head
rotated = rotate(ans, ans.index(unbalancedOut))

print "->".join(map(str,rotated))




