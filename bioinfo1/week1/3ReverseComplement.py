def ReverseComplement(pattern):
    complement_set = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join([complement_set[item] for item in pattern[::-1]])

