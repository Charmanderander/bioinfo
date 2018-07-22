def SpectralConvolution(spectrum):
    spectrum = sorted(spectrum)
    differenceDict = {}
    for i in range(len(spectrum)):
        if spectrum[i] not in differenceDict:
            differenceDict[spectrum[i]] = []
        for j in range(i+1):
            difference = spectrum[i] - spectrum[j]
            if difference != 0:
                differenceDict[spectrum[i]].append(difference)

    return differenceDict

if __name__ == "__main__":
    '''
    with open("data.txt", "r") as f:
        data = f.readlines()

    cleanData = list(map(int,data[0].replace("\n","").split(" ")))
    '''

    spectrum = [0, 57, 118, 179, 236, 240, 301]

    spectralDict = SpectralConvolution(spectrum)
    totalMass = []

    for key in spectralDict:
        for mass in spectralDict[key]:
            totalMass.append(mass)

    print(" ".join(list(map(str, sorted(totalMass)))))
