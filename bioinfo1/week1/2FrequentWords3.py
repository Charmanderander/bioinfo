import re
import numpy as np

# fill in your FrequentWords() function here along with any subroutines you need.
def FrequentWords(Text, k):
    freq_pat = []
    
    freq_arr = 

    count = [{findPattern(Text, Text[i:i+k]):Text[i:i+k]} for i in range(len(Text)-k+1)]

    df_count = pd.DataFrame(count)

    return df_count.iloc[:,-1].dropna().drop_duplicates().tolist()

def findPattern(string, pattern):
    matches = re.findall(r'(?=('+pattern+'))',string)
    return len(matches)

print FrequentWords("CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT", 3)
