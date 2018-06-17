import math
from fileReader import fileReader

sym = {0:"A", 1:"C", 2:"G", 3:"T"}

def MedianString(Dna, k):
    Median = ""
    distance = 999
    for x in range(int(math.pow(4,k))):
        Pattern = NumberToPattern(x,k)
        curDist = DistanceBetweenPatternAndStrings(Pattern, Dna)
        print "###"
        print "Pattern: " + Pattern
        print "curDis: " + str(curDist) + " distance: " + str(distance)
        if curDist < distance:
            distance = curDist
            Median = Pattern

    return Median

def DistanceBetweenPatternAndStrings(pattern, dna):
    k = len(pattern)
    distance = 0
    for string in dna:
        HamD = len(pattern) + 1
        for x in range(len(string) - k + 1):
            kmer = string[x:x+k]
            patternD = HammingDistance(pattern, kmer)
            if patternD < HamD:
                HamD = patternD
        distance += HamD

    return distance

def HammingDistance(p, q):
    count = 0
    for x in range(len(p)):
        if p[x] != q[x]:
            count += 1
    return count

def NumberToPattern(index, k):
    if(k == 1):
        return sym[index]
    prefixIndex = int(index/4)
    r = index % 4
    symbol = sym[r]
    PrefixPattern = NumberToPattern(prefixIndex, k-1)
    return PrefixPattern + symbol

stringList = fileReader()

print stringList

k = 3

print MedianString(stringList, k)
