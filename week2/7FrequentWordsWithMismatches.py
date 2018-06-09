import math

syms = ["A", "C", "G", "T"]
symDic1 = {"A":0, "C":1, "G":2, "T":3}
symDic2 = {0:"A", 1:"C", 2:"G", 3:"T"}


def FrequentWordsWithMismatches(Text, k, d):
    FrequentPatterns = []
    freq_arr = {}
    NeighborhoodsArray = []

    for i in range(len(Text) - k + 1):
        Neighborhoods = Neighbors(Text[i:i+k],d)
        tmpArr = [x for x in Neighborhoods]
        for item in tmpArr:
            NeighborhoodsArray.append(item)

    for i in range(int(math.pow(4,k))):
            freq_arr[i] = 0

    for i in range(len(NeighborhoodsArray)):
        Pattern = NeighborhoodsArray[i]
        j = PatternToNumber(Pattern)
        freq_arr[j] = freq_arr[j] + 1

    max_count = max(freq_arr.values())

    for i in range(int(math.pow(4,k))):
        if(freq_arr[i] == max_count):
            Pattern = NumberToPattern(i,k)
            FrequentPatterns.append(Pattern)

    return FrequentPatterns 
                

def Neighbors(Pattern, d):
    if d == 0:
        return Pattern
    if len(Pattern) == 1:
        return {"A", "C", "G", "T"}

    Neighborhood = []

    SuffixNeighbors = Neighbors(Pattern[1:], d)

    for Text in SuffixNeighbors:
        if (HammingDistance(Pattern[1:], Text) < d):
            for x in syms:
                Neighborhood.append(x+Text)
        else:
            Neighborhood.append(Pattern[0]+Text)

    return Neighborhood

def HammingDistance(p, q):
    count = 0
    for x in range(len(p)):
        if p[x] != q[x]:
            count += 1
    return count

def PatternToNumber(Pattern):
    if (Pattern == ""):
        return 0
    symbol = Pattern[-1]
    Prefix = Pattern[:-1]
    return 4 * PatternToNumber(Prefix) + SymbolToNumber(symbol)

def SymbolToNumber(symbol):
    return symDic1[symbol]

def NumberToPattern(index, k):
    if(k == 1):
        return symDic2[index]
    prefixIndex = int(index/4)
    r = index % 4
    symbol = symDic2[r]
    PrefixPattern = NumberToPattern(prefixIndex, k-1)
    return PrefixPattern + symbol

Text = "ACTAACTACGCTGAAAACTATCGCACTAACTAACTATCGCACTAGAAAGAAAACTAGAAACGCTGAAAACTAACTACGCTAGAAGACGCTTCGCACTACGCTAGAAGACGCTCGCTAGATCGCACTAACTAAGACGCTAGAAGATCGCAGAACTAACTACGCTGAAATCGCAGACGCTTCGCTCGCACTAAGAAGAAGAACTATCGCACTAGAAACGCTGAAACGCTACTAGAAAAGAGAAAAGAGAAAAGAACTAACTAACTAGAAACGCTACTATCGCACTACGCTGAAATCGCGAAAAGAGAAACGCTAGAGAAAAGAACTAAGACGCTAGAACTACGCTTCGCTCGCAGAACTACGCTAGAGAAAAGAAGAAGAGAAAAGACGCTTCGC"
k = 7
d = 3

print FrequentWordsWithMismatches(Text, k, d)
