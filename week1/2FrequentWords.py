def FrequentWords(string, k):
    length_str = len(string)
    count = []
    freq_pat = []

    for i in range(length_str-k+1):
        string_pat = string[i:i+k]
        count.append(findPattern(string, string_pat))

    print count
    
    maxCount = max(count)

    for x in range(length_str-k+1):
        if count[x] == maxCount:
            freq_pat.append(string[x:x+k])

    freq_pat_set = set(freq_pat)

    return len(freq_pat_set), freq_pat_set

def findPattern(string, pattern):
    length_str = len(string)
    length_pat = len(pattern)
    count = 0
    for i in range(length_str-length_pat+1):
        string_pat = string[i:i+length_pat]
        if string_pat == pattern:
            count += 1
    return count

