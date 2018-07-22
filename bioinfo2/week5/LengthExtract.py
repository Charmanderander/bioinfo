contigFile = "25.node"

def LengthExtract(lines):
    length = []
    for line in lines:
        items = line.split("_")
        length.append(int(items[3]))
    return length

if __name__ == "__main__":
    with open(contigFile, "r") as f:
        data = f.readlines()

    lengths = LengthExtract(data)

    totalLength = 0
    longCount = 0
    longLength = 0

    for length in lengths:
        if length >= 1000:
            longCount += 1
            longLength += length
        totalLength += length

    minimumLen = totalLength / 2

    addedLength = 0

    for length in lengths:

        addedLength += length
        if addedLength >= minimumLen:
            print(length)
            break

    print(totalLength)

    print("long stats")
    print(longCount)
    print(longLength)
