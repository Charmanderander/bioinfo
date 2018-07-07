import re
import math
import itertools

sym1 = {"A":0, "C":1, "G":2, "T":3}
sym2 = {0:"A", 1:"C", 2:"G", 3:"T"}

def ClumpFinding(Genome, k, L, t):
    freq_pat = []
    clump = {}

    for i in range(int(math.pow(4,k))):
        clump[i] = 0

    Text = Genome[0:L]
    freq_arr = computing_frequencies(Text, k)

    for i in range(int(math.pow(4,k))):
        if freq_arr[i] >= t:
            clump[i] = 1

    for i in range(1, len(Genome) - L +1):
        FirstPattern = Genome[i:i+k]
        index = PatternToNumber(FirstPattern)
        freq_arr[index] -= 1
        LastPattern = Genome[i+L-k:i+L]
        index = PatternToNumber(LastPattern)
        freq_arr[index] += 1

        if freq_arr[index] >= t:
            clump[index] = 1

    for i in range(int(math.pow(4,k))):
        if clump[i] == 1:
            Pattern = NumberToPattern(i,k)
            freq_pat.append(Pattern)

    return freq_pat

def computing_frequencies(Text,k):
    freq_arr = {}

    for i in range(int(math.pow(4,k))):
        freq_arr[i] = 0

    for i in range(len(Text) - k + 1):
        Pattern = Text[i:i+k]
        j = PatternToNumber(Pattern)
        freq_arr[j] = freq_arr[j] + 1

    return freq_arr.values()

def PatternToNumber(Pattern):
    if (Pattern == ""):
        return 0
    return 4 * PatternToNumber(Pattern[:-1]) + sym1[Pattern[-1]]

def NumberToPattern(index, k):
    if(k == 1):
        return sym2[index]
    return NumberToPattern(int(index/4), k-1) + sym2[index % 4]
