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

def CyclicSpectrum(peptide):
    prefixMass = [0]
    cyclicSpectrum = []

    for i in range(len(peptide)):
        previousMass = prefixMass[i]
        currentMass = mass[peptide[i]]
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

def Score(experimental, theory):
    ansDict = {}
    score = 0

    for item in experimental:
        if item in theory:
            theory.remove(item)
            if item not in ansDict:
                ansDict[item] = 1
            else:
                ansDict[item] += 1

    for key in ansDict:
        score += ansDict[key]

    return score

with open("data.txt", "r") as f:
    data = f.readlines()

peptide = data[0].replace("\n",'')

theoryList = list(map(int, data[1].replace("\n",'').split(" ")))


questionList = [peptide]

for qns in questionList:
    print("Processing " + qns)
    ansList = CyclicSpectrum(qns)

score = Score(ansList, theoryList)

print score 
