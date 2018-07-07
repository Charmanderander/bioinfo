import itertools
import operator

nucleotide = ["A","C","G","T"]

def GreedyMotifSearch(Dna, k, t):
    firstDna = Dna[0]

    bestMotif = [string[:k] for string in Dna]

    for x in range(len(firstDna) - k + 1):
        kmer = firstDna[x:x+k]
        candidateMotif = []
        candidateMotif.append(kmer)

        for y in range(1,t):
            profile = ProfileMaker(candidateMotif)

            probableKmer = ProfileMostProbableKmer(Dna[y], k, profile)
            candidateMotif.append(probableKmer)

        if (Score(bestMotif) > Score(candidateMotif)):
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
    # get an iterable of (item, iterable) pairs
    SL = sorted((x, i) for i, x in enumerate(L))
    # print 'SL:', SL
    groups = itertools.groupby(SL, key=operator.itemgetter(0))
    # auxiliary function to get "quality" for an item
    def _auxfun(g):
        item, iterable = g
        count = 0
        min_index = len(L)
        for _, where in iterable:
            count += 1
        min_index = min(min_index, where)
      # print 'item %r, count %r, minind %r' % (item, count, min_index)
        return count, -min_index
    # pick the highest-count/earliest item
    return max(groups, key=_auxfun)[0]

def ProfileMostProbableKmer(text, k, profile):
    text = text.strip()
    probDict = {}

    initialProbKmer = text[:k]

    for x in range(len(text) - k + 1):
        kmer = text[x:x+k]
        stringProb = 1
        for idx, x in enumerate(kmer):
            prob = profile[x][idx]
            stringProb *= float(prob)

        probDict[kmer] = stringProb

    probKmer = max(probDict, key=probDict.get)
    
    if (probDict[probKmer] == 0):
        probKmer = initialProbKmer

    return probKmer
