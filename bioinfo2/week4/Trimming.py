import operator

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

def Score(theory, experimental):
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

def Trim(LeaderBoard, spectrum, N):
    scoreDict = {}

    for idx, candidate in enumerate(LeaderBoard):
        candidateSpectrum = LinearSpectrum(candidate)
        score = Score(candidate,spectrum)
        scoreDict[idx] = score

    sortedList = sorted(scoreDict.iteritems(), \
                   key=operator.itemgetter(1), \
                   reverse=True)

    keysToKeep = []

    for i in range(N):
        keysToKeep.append(sortedList[i][0])

    for j in range(N, len(LeaderBoard)):
        if sortedList[j][1] == sortedList[N-1][1]:
            keysToKeep.append(sortedList[j][0])
        else:
            break

    return keysToKeep
    
with open("data.txt", "r") as f:
    data = f.readlines()

questionList = data[0].replace('\n','').split(" ")
theoryList = list(map(int, data[1].replace('\n','').split(" ")))
n = int(data[2].replace("\n",""))

ansList = []

for qns in questionList:
    print("Processing " + qns)
    ans = LinearSpectrum(qns)
    ansList.append(ans)

trimmedIndex = Trim(ansList, theoryList, n)

for index in trimmedIndex:
    print questionList[index]
