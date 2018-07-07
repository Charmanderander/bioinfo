def fileReader(delimiter="\n"):
    stringList = []

    with open("file.txt", "r") as f:
        data = f.readlines()
        for line in data:
            stringList.append(line)
    return stringList

