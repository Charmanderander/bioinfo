def PatternToNumber(Pattern):
    if (Pattern == ""):
        return 0
    symbol = Pattern[-1]
    Prefix = Pattern[:-1]
    return 4 * PatternToNumber(Prefix) + SymbolToNumber(symbol)

def SymbolToNumber(symbol):
    sym = {"A":0, "C":1, "G":2, "T":3}
    return sym[symbol]

'''
Faster implementation

sym = {"A":0, "C":1, "G":2, "T":3}

def PatternToNumber(Pattern):
    if (Pattern == ""):
        return 0
    return 4 * PatternToNumber(Pattern[:-1]) + sym[Pattern[-1]]
'''

print PatternToNumber("CCGCATGCATCGGCCACTCA")
