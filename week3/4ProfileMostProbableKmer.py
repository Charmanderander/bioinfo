def ProfileMostProbableKmer(text, k, profile):

    probDict = {}

    for x in range(len(text) - k + 1):
        kmer = text[x:x+k]
        stringProb = 1
        for idx, x in enumerate(kmer):
            prob = profile[x][idx]
            stringProb *= float(prob)
        
        probDict[kmer] = stringProb        

    return max(probDict, key=probDict.get)
