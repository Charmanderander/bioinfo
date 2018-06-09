
def MinimumSkew(Genome):
    skewList = []
    minSkewList = []
    skew = 0
    for i in Genome:
        if i == "C":
            skew -= 1
        elif i == "G":
            skew += 1
        skewList.append(skew)

    minSkew = min(skewList)

    for i,x in enumerate(skewList):
        if x == minSkew:
            minSkewList.append(i +1)

    return minSkewList

with open("text.txt") as f:
    data = f.read()
    print MinimumSkew(data)

