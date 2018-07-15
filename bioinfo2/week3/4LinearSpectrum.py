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


questionList = ["ETC","QCV","TCQ","AVQ","TVQ","TCE"]

for qns in questionList:
    print("Processing " + qns)
    ansList = LinearSpectrum(qns)

    for ans in ansList:
        print(ans)

    print("###")

