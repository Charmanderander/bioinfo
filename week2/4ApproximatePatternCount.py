def ApproximatePatternCount(Text, Pattern, d):
    positions = [] # initializing list of positions
    for x in range(len(Text)-len(Pattern)+1):
        curPattern = Text[x:x+len(Pattern)]
        if HammingDistance(Pattern, curPattern) <= d:
            positions.append(x)
    # your code here
    return len(positions)

def HammingDistance(p, q):
    count = 0
    for x in range(len(p)):
        if p[x] != q[x]:
            count += 1
    return count
    count = 0 # initialize count variable
    # your code here
    return count

print ApproximatePatternCount("GGACCTCAACCGGGTCTGACATGTTTGCCTGTGTGCGTGCACGACCCTAGGGCCATTTGGGTCTACTTATATTCGACGAACGAGATATCGCTGCTGTTCGTCTCAGAATCGGGCAAGTCATGGGAAATCGACGTAACGGGTTCCTGATTACGCACCCTACGATCGTAAACGGTGTTGCTGCTCGCGATAAAACCCGGATCCAGAGCACTAGCATAGATGGTTACGGAGTTTATACCGATATACGAGTCTCCGGATTATAGTTAGTAGACACTAGACACTGCTACCTCTAACCCCTTCATCGGACACCAGGTCGCTATGTTCACTGCGTGGCGAGTGCAAGAAAAGCATAATCATTAGCCCGGTGAAGAGATATACTATAGCTCTACCGGTGATCCTTCC", "GGTGA", 3)
