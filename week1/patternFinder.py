def findPattern(string, pattern):
    length_str = len(string)
    length_pat = len(pattern)
    count = 0
    for i in range(length_str-length_pat+1):
        string_pat = string[i:i+length_pat]
        if string_pat == pattern:
            count += 1
    return count

'''
Faster solution

import re

def PatternCount(Text, Pattern):
    # fill in your function here
    matches = re.findall(r'(?=('+Pattern+'))',Text)
    
    return len(matches)

'''

print findPattern("CGCGATACGTTACATACATGATAGACCGCGCGCGATCATATCGCGATTATC", "CGCG")
