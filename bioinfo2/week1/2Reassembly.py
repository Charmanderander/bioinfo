from fileReader import fileReader
def Reassemble(strings):
    finalString = strings[0]
    del strings[0]
    for string in strings:
        finalString += string[-1]

    return finalString

stringList = fileReader()

print Reassemble(stringList)
