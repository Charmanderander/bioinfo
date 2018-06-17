syms = ["A", "C", "G", "T"]


def Neighbors(Pattern, d):
    if d == 0:
        return Pattern
    if len(Pattern) == 1:
        return {"A", "C", "G", "T"}

    Neighborhood = []

    SuffixNeighbors = Neighbors(Pattern[1:], d)

    for Text in SuffixNeighbors:
        if (HammingDistance(Pattern[1:], Text) < d):
            for x in syms:
                Neighborhood.append(x+Text)
        else:
            Neighborhood.append(Pattern[0]+Text)

    return Neighborhood

def HammingDistance(p, q):
    count = 0
    for x in range(len(p)):
        if p[x] != q[x]:
            count += 1
    return count

print len(Neighbors("TGCAT",2))
            
                
