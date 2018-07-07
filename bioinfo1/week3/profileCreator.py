nucleotide = ['A', 'C', 'G', 'T']

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

motif = ["GGC", "AAG"]

print ProfileMaker(motif)
