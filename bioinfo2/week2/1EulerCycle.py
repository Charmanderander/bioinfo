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
    reversedPath = GeneratePath(adjDict,path, stack, 2)
    path = reversedPath[::-1]
    
    return path
    

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


adjDict = {}
data = sys.stdin.read().split('\n')
for item in data:
        adjDict[int(item.split("->")[0])] = list(map(int,item.split("->")[1].strip().split(",")))
        
ans = EulerCycle(adjDict)
print("->".join(map(str,ans)))
CheckEuler(adjDict)
ans = EulerCycle(adjDict)

print "->".join(map(str,ans))





