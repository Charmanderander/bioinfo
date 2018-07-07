sym = {0:"A", 1:"C", 2:"G", 3:"T"}

def NumberToPattern(index, k):
    if(k == 1):
        return sym[index]
    prefixIndex = int(index/4)
    r = index % 4
    symbol = sym[r]
    PrefixPattern = NumberToPattern(prefixIndex, k-1)
    return PrefixPattern + symbol

'''
Faster Implementation

sym = {0:"A", 1:"C", 2:"G", 3:"T"}

def NumberToPattern(index, k):
    if(k == 1):
        return sym[index]
    return NumberToPattern(int(index/4), k-1) + sym[index % 4]
'''
