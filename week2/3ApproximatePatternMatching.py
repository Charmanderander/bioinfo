def ApproximatePatternMatching(Text, Pattern, d):
    positions = [] # initializing list of positions
    for x in range(len(Text)-len(Pattern)+1):
        curPattern = Text[x:x+len(Pattern)]
        if HammingDistance(Pattern, curPattern) <= d:
            positions.append(x)
    # your code here
    return positions

def HammingDistance(p, q):
    count = 0
    for x in range(len(p)):
        if p[x] != q[x]:
            count += 1
    return count

ans = []
'''
with open("file.txt") as f:
    data = f.readline().strip('\n')
'''
for i in ApproximatePatternMatching("AACAAGCTGATAAACATTTAAAGAG","AAAAA" , 2):
        ans.append(i)

print len(ans)
