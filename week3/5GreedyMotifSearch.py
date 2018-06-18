from fileReader import fileReader
import itertools
import operator

nucleotide = ["A","C","G","T"]

def GreedyMotifSearch(Dna, k, t):
    firstDna = Dna[0]

    bestMotif = [string[:k] for string in Dna]

    for x in range(len(firstDna) - k):
        kmer = firstDna[x:x+k]
        candidateMotif = []
        candidateMotif.append(kmer)

        for y in range(1,t):
            profile = ProfileMaker(candidateMotif)

            print "###"
            print candidateMotif
            print profile

            probableKmer = ProfileMostProbableKmer(Dna[y], k, profile)
            print "Probable kmer is " + probableKmer
            candidateMotif.append(probableKmer)

        if (Score(bestMotif) < Score(candidateMotif)):
            bestMotif = candidateMotif

    return bestMotif

def Score(motif):
    listedMotif = []
    motifScore = 0

    for string in motif:
        listedMotif.append([char for char in string])
    transposedMotif = zip(*listedMotif)

    for item in transposedMotif:
        mostCommon = MostCommon(item)
        count = item.count(mostCommon)
        colScore = len(item) - count
        motifScore += colScore

    return motifScore

def ProfileMaker(motif):
    nucCollection = []
    profile = {"A":[], "C":[], "G":[], "T":[]}

    for i in motif[0]:
        nucCollection.append([])

    for kmer in motif:
        for idx, nuc in enumerate(kmer):
            nucCollection[idx].append(nuc)

    for idx, nucCol in enumerate(nucCollection):
        for nuc in nucleotide:
            probability = (float(nucCol.count(nuc)) / float(len(nucCol)))
            profile[nuc].append(probability)

    return profile

def MostCommon(L):
  groups = itertools.groupby(sorted(L))
  def _auxfun((item, iterable)):
    return len(list(iterable)), -L.index(item)
  return max(groups, key=_auxfun)[0]

def ProfileMostProbableKmer(text, k, profile):
    text = text.strip()
    probDict = {}

    for x in range(len(text) - k + 1):
        kmer = text[x:x+k]
        stringProb = 1
        for idx, x in enumerate(kmer):
            prob = profile[x][idx]
            stringProb *= float(prob)

        probDict[kmer] = stringProb

    return max(probDict, key=probDict.get)


stringList = fileReader()
k = 3
t = 5

print GreedyMotifSearch(stringList, k, t)
