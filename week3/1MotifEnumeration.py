syms = ["A", "C", "G", "T"]

# Write your MotifEnumeration() function here along with any subroutines you need.
# This function should return a list of strings.
def MotifEnumeration(dna, k, d):
    Pattern = []
    PresentDict = {}

    for x in range (len(dna[0])-k+1):
        FirstStringPat = dna[0][x:x+k]
        Neighborhood = Neighbors(FirstStringPat, d)
        for kmer in Neighborhood: #going through each kmer
            for j in range(len(dna)):
                PresentDict[j] = 0
            for idx,dnaString in enumerate(dna): #going through each string
                for i in range (len(dnaString)-k+1): #going through each pattern
                    dnaPattern = dnaString[i:i+k]
                    if (HammingDistance(kmer, dnaPattern) <= d):
                        #if variant pattern occurs in the string
                        PresentDict[idx] = 1
            
            if 0 not in PresentDict.values():
                Pattern.append(kmer)

    Pattern = set(Pattern)
    return list(Pattern)


def Neighbors(Pattern, d):
    if d == 0:
        return [Pattern]
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




setStrings = ["ATTTGGC",
              "TGCCTTA",
              "CGGTATC",
              "GAAAATT"
             ]
k = 3
d = 1

print MotifEnumeration(setStrings, k, d)
