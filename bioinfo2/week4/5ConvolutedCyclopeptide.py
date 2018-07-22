import copy
import operator

def LeaderboardCyclopeptideSequencing(spectrum, n):
    spectrum = sorted(spectrum)
    leaderBoard = []
    tmpList = []

    leaderPeptide = [0]
    scoreLeader = 0

    leaderPeptideCollection = {}

    for item in mass.values():
        tmpList.append(item)

    for item in tmpList:
        leaderBoard.append([item])

    while len(leaderBoard) != 0:

        leaderBoard = Expand(leaderBoard)
        tmpLeaderBoard = copy.deepcopy(leaderBoard)

        for peptide in leaderBoard:
            if Mass(peptide) == spectrum[-1]:
                peptideSpectrum = CyclicSpectrum(peptide)
                scorePeptide = Score(peptideSpectrum, spectrum) 

                if scorePeptide >= scoreLeader:
                    scoreLeader = scorePeptide

                    if scorePeptide not in leaderPeptideCollection:
                        leaderPeptideCollection[scorePeptide] = [peptide]
                    else:
                        leaderPeptideCollection[scorePeptide].append(peptide)

            elif Mass(peptide) > spectrum[-1]:
                tmpLeaderBoard.remove(peptide)

        trimmedIndex = Trim(tmpLeaderBoard, spectrum, n)

        trimmedList = []

        for index in trimmedIndex:
            trimmedList.append(tmpLeaderBoard[index])

        leaderBoard = trimmedList

    return leaderPeptideCollection

def Trim(leaderBoard, spectrum, N):
    scoreDict = {}

    for idx, candidate in enumerate(leaderBoard):
        candidateSpectrum = LinearSpectrum(candidate)
        score = Score(candidateSpectrum,spectrum)
        scoreDict[idx] = score

    sortedList = sorted(scoreDict.items(), \
                   key=operator.itemgetter(1), \
                   reverse=True)

    masses = []

    if N > len(leaderBoard):
        for i in range(len(leaderBoard)):
            masses.append(sortedList[i][0])
    else:
        for i in range(N):
            masses.append(sortedList[i][0])

        for j in range(N, len(leaderBoard)):
            if sortedList[j][1] == sortedList[N-1][1]:
                masses.append(sortedList[j][0])
            else:
                break

    return masses

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

def Score(experimental,theory):
    ansDict = {}
    score = 0

    theoryCopy = list(theory)

    for item in experimental:
        if item in theoryCopy:
            theoryCopy.remove(item)
            if item not in ansDict:
                ansDict[item] = 1
            else:
                ansDict[item] += 1

    for key in ansDict:
        score += ansDict[key]

    return score

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

def SpectralConvolution(spectrum, M):
    spectrum = sorted(spectrum)
    differenceDict = {}
    multiplicityDict = {}
    convMasses = []
    numKeys = 0

    for i in range(len(spectrum)):
        if spectrum[i] not in differenceDict:
            differenceDict[spectrum[i]] = []
        for j in range(i+1):
            difference = spectrum[i] - spectrum[j]
            if difference != 0:
                differenceDict[spectrum[i]].append(difference)

    for key in differenceDict:
        for diff in differenceDict[key]:
            if diff >= 57 and diff <200:
                if diff not in multiplicityDict:
                    multiplicityDict[diff] = 1
                else:
                    multiplicityDict[diff] += 1

    sortedList = sorted(multiplicityDict.items(), \
                   key=operator.itemgetter(1), \
                   reverse=True)

    numKeys = len(list(multiplicityDict.keys()))

    if M > numKeys:
        for i in range(numKeys):
            convMasses.append(sortedList[i][0])
    else:
        for i in range(M):
            convMasses.append(sortedList[i][0])

        for j in range(M, numKeys):
            if sortedList[j][1] == sortedList[M-1][1]:
                convMasses.append(sortedList[j][0])
            else:
                break

    return convMasses


with open("data.txt", "r") as f:
    data = f.readlines()

M = int(data[0].replace("\n",""))

N = int(data[1].replace("\n",""))

spectrum = list(map(int, data[2].strip().replace('\n','').split()))

convolutedMass = SpectralConvolution(spectrum, M)

mass = {}

for i in sorted(convolutedMass):
    mass[i] = i

ansList = LeaderboardCyclopeptideSequencing(spectrum,N)

maxKey = max(list(ansList.keys()))

count = 0

listLen = {}

for item in ansList[maxKey]:
    if len(item) not in listLen:
        listLen[len(item)] = [item]
    else:
        listLen[len(item)].append(item)

for key in listLen:
    for item in sorted(listLen[key]):
        count += 1
        print("-".join(list(map(str,item))))

print(count)
