import copy

mass = {
        "G" : 57,
        "A" : 71,
        "S" : 87,
        "P" : 97,
        "V" : 99,
        "T" : 101,
        "C" : 103,
        "I" : 113,
        "L" : 113,
        "N" : 114,
        "D" : 115,
        "K" : 128,
        "Q" : 128,
        "E" : 129,
        "M" : 131,
        "H" : 137,
        "F" : 147,
        "R" : 156,
        "Y" : 163,
        "W" : 186,
        }

def CyclopeptideSequencing(spectrum):
    peptides = []
    tmpList = []

    finalPeptides = []

    for item in spectrum:
        if item in mass.values() and item not in tmpList:
            tmpList.append(item)

    for item in tmpList:
        peptides.append([item])

    while len(peptides) != 0:

        peptides = Expand(peptides)
        tmpPeptides = copy.deepcopy(peptides)
        
        for peptide in peptides:
            if Mass(peptide) >= spectrum[-1]:
                if CyclicSpectrum(peptide) == spectrum:
                    finalPeptides.append(peptide)
                tmpPeptides.remove(peptide)
            
            elif not Consistency(LinearSpectrum(peptide), spectrum):
                tmpPeptides.remove(peptide)

        peptides = tmpPeptides

    return finalPeptides

def CyclicSpectrum(peptide):
    prefixMass = [0]
    cyclicSpectrum = []

    for i in range(len(peptide)):
        previousMass = prefixMass[i]
        currentMass = peptide[i]
        prefixMass.append(previousMass + currentMass)

    peptideMass = prefixMass[len(peptide)]

    for i in range(len(peptide)):
        for j in range(i+1,len(peptide)+1,1):
            massDifference = prefixMass[j] - prefixMass[i]
            cyclicSpectrum.append(massDifference)
            if i > 0 and j < len(peptide):
                CyclicMassDifference = peptideMass - massDifference
                cyclicSpectrum.append(CyclicMassDifference)

    cyclicSpectrum.append(0)

    return sorted(cyclicSpectrum)

def LinearSpectrum(peptide):
    prefixMass = [0]
    linearSpectrum = []

    for i in range(len(peptide)):
        previousMass = prefixMass[i]
        currentMass = peptide[i]
        prefixMass.append(previousMass + currentMass)

    for i in range(len(peptide)):
        for j in range(i+1,len(peptide)+1,1):
            massDifference = prefixMass[j] - prefixMass[i]
            linearSpectrum.append(massDifference)

    linearSpectrum.append(0)

    return sorted(linearSpectrum)

def Consistency(peptide, spectrum):
    seen = []

    for item in peptide:
        if item not in seen:
            seen.append(item)
            peptideCount = peptide.count(item)
            spectrumCount = spectrum.count(item)

            if peptideCount > spectrumCount:
                return False

    return True

def Mass(peptide):
    totalMass = 0

    for item in peptide:
        totalMass += item

    return totalMass

def Expand(peptides):
    expandedPeptide = []

    for items in peptides:
        for masses in mass.values():
            expandedItem = []
            for item in items:
                expandedItem.append(item)
            expandedItem.append(masses)
            expandedPeptide.append(expandedItem)

    return expandedPeptide

with open("data.txt", "r") as f:
    data = f.readline()

spectrum = list(map(int, data.strip().replace('\n','').split()))

ansList = CyclopeptideSequencing(spectrum)

seen = []

for ans in ansList:
    if ans not in seen:
        seen.append(ans)
        print("-".join(list(map(str, ans))))
