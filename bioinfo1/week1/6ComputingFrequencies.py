import math

sym = {"A":0, "C":1, "G":2, "T":3}

def ComputingFrequencies(Text,k):
    freq_arr = {}

    for i in range(int(math.pow(4,k))):
        freq_arr[i] = 0

    for i in range(len(Text) - k + 1):
        Pattern = Text[i:i+k]
        j = PatternToNumber(Pattern)
        freq_arr[j] = freq_arr[j] + 1

    return freq_arr

def PatternToNumber(Pattern):
    if (Pattern == ""):
        return 0
    return 4 * PatternToNumber(Pattern[:-1]) + sym[Pattern[-1]]

