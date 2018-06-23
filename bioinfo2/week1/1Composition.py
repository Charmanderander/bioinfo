
def Composition(Text,k):
    collection = []
    for i in range(len(Text) - k + 1):
        collection.append(Text[i:i+k])
    collection.sort()
    return collection

