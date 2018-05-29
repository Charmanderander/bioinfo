import re

# fill in your PatternMatching() function along with any subroutines that you need.
def PatternMatching(Pattern, Genome):
    match=[]
    for m in re.finditer(r'(?=('+Pattern+'))',Genome):
         match.append(m.start())
    return match

print PatternMatching("ATA", "GACGATATACGACGATA")

'''
Faster implementation

import re

# fill in your PatternMatching() function along with any subroutines that you need.
def PatternMatching(Pattern, Genome):
    return [m.start() for m in re.finditer(r'(?=('+Pattern+'))',Genome)]
'''

