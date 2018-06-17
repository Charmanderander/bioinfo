from fileReader import fileReader

# Write your DistanceBetweenPatternAndStrings() function here along with any subroutines that you need.
# dna is a list of strings.
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

stringList = fileReader()

pattern = "GTGTG"

print DistanceBetweenPatternAndStrings(pattern, stringList)
