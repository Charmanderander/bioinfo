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

def LinearSpectrum(peptide):
    prefixMass = [0]
    linearSpectrum = []

    for i in range(len(peptide)):
        previousMass = prefixMass[i]
        currentMass = mass[peptide[i]]
        prefixMass.append(previousMass + currentMass)

    for i in range(len(peptide)):
        for j in range(i+1,len(peptide)+1,1):
            massDifference = prefixMass[j] - prefixMass[i]
            linearSpectrum.append(massDifference)

    linearSpectrum.append(0)

    return sorted(linearSpectrum)

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

'''
with open("data.txt", "r") as f:
    data = f.readlines()

peptide = data[0].replace("\n",'')

theoryList = list(map(int, data[1].replace("\n",'').split(" ")))
'''

cyclicquestionList = ["MAMA"]

cyclictheoryList = [0, 57, 71, 71, 71, 104, 131, 202, 202, 202, 256, 333, 333, 403, 404]

linearquestionList = ["PEEP"]

lineartheoryList = [0, 97, 97, 129, 194, 196, 226, 226, 244, 258, 323, 323, 452]

for qns in linearquestionList:
    print("Processing " + qns)
    ansList = LinearSpectrum(qns)

score = Score(ansList, lineartheoryList)

print(score)
