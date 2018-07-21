import copy
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

def LeaderboardCyclopeptideSequencing(spectrum, n):
    leaderBoard = []
    tmpList = []

    leaderPeptide = [0]

    for item in mass.values():
            tmpList.append(item)

    for item in tmpList:
        leaderBoard.append([item])

    while len(leaderBoard) != 0:

        leaderBoard = Expand(leaderBoard)
        tmpLeaderBoard = copy.deepcopy(leaderBoard)

        for peptide in leaderBoard:
            if Mass(peptide) == spectrum[-1]:
                peptideSpectrum = LinearSpectrum(peptide)
                leaderPeptideSpectrum = LinearSpectrum(leaderPeptide)
                if Score(peptideSpectrum, spectrum) > Score(leaderPeptideSpectrum, spectrum):
                    leaderPeptide = peptide
            elif Mass(peptide) > spectrum[-1]:
                tmpLeaderBoard.remove(peptide)

        trimmedIndex = Trim2(tmpLeaderBoard, spectrum, n)

        trimmedList = []

        for index in trimmedIndex:
            trimmedList.append(tmpLeaderBoard[index])

        leaderBoard = trimmedList

    return leaderPeptide

def Trim2(LeaderBoard, spectrum, N):
    scoreDict = {}

    for idx, candidate in enumerate(LeaderBoard):
        candidateSpectrum = LinearSpectrum(candidate)
        score = Score(candidate,spectrum)
        scoreDict[idx] = score

    sortedList = sorted(scoreDict.iteritems(), \
                   key=operator.itemgetter(1), \
                   reverse=True)

    keysToKeep = []

    if N > len(LeaderBoard):
        for i in range(len(LeaderBoard)):
            keysToKeep.append(sortedList[i][0])
    else:
        for i in range(N):
            keysToKeep.append(sortedList[i][0])

    for j in range(N, len(LeaderBoard)):
        if sortedList[j][1] == sortedList[N-1][1]:
            keysToKeep.append(sortedList[j][0])
        else:
            break

    return keysToKeep

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

    theoryCopy = copy.deepcopy(theory)

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

with open("data.txt", "r") as f:
    data = f.readlines()

n = int(data[0].replace("\n",""))

spectrum = list(map(int, data[1].strip().replace('\n','').split()))

ansList = LeaderboardCyclopeptideSequencing(spectrum,n)

print "-".join(list(map(str,ansList)))
