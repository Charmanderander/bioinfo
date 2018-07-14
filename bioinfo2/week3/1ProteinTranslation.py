geneticNames = {
        "AAA" : 0, "AAC" : 1, "AAG" : 2, "AAU" : 3, "ACA" : 4,
        "ACC" : 5, "ACG" : 6, "ACU" : 7, "AGA" : 8, "AGC" : 9,
        "AGG" : 10, "AGU" : 11, "AUA" : 12,  "AUC" : 13, "AUG" : 14,
        "AUU" : 15, "CAA" : 16, "CAC" : 17, "CAG" : 18, "CAU" : 19,
        "CCA" : 20, "CCC" : 21, "CCG" : 22, "CCU" : 23, "CGA" : 24,
        "CGC" : 25, "CGG" : 26, "CGU" : 27, "CUA" : 28, "CUC" : 29,
        "CUG" : 30, "CUU" : 31, "GAA" : 32, "GAC" : 33, "GAG" : 34,
        "GAU" : 35, "GCA" : 36, "GCC" : 37, "GCG" : 38, "GCU" : 39,
        "GGA" : 40, "GGC" : 41, "GGG" : 42, "GGU" : 43, "GUA" : 44,
        "GUC" : 45, "GUG" : 46, "GUU" : 47, "UAA" : 48, "UAC" : 49,
        "UAG" : 50, "UAU" : 51, "UCA" : 52, "UCC" : 53, "UCG" : 54,
        "UCU" : 55, "UGA" : 56, "UGC" : 57, "UGG" : 58, "UGU" : 59,
        "UUA" : 60, "UUC" : 61, "UUG" : 62, "UUU" : 63, 
              }

geneticCode = {
              0 : "K", 1 : "N", 2 : "K", 3 : "N", 4 : "T",
              5 : "T", 6 : "T", 7 : "T", 8 : "R", 9 : "S",
              10 : "R", 11 : "S", 12 : "I",  13: "I", 14 : "M",
              15 : "I", 16 : "Q", 17 : "H", 18 : "Q", 19 : "H",
              20 : "P", 21 : "P", 22 : "P", 23 : "P", 24 : "R",
              25 : "R", 26 : "R", 27 : "R", 28 : "L", 29 : "L",
              30 : "L", 31 : "L", 32 : "E", 33 : "D", 34 : "E",
              35 : "D", 36 : "A", 37 : "A", 38 : "A", 39 : "A",
              40 : "G", 41 : "G", 42 : "G", 43 : "G", 44 : "V",
              45 : "V", 46 : "V", 47 : "V", 48 : "*", 49 : "Y",
              50 : "*", 51 : "Y", 52 : "S", 53 : "S", 54 : "S",
              55 : "S", 56 : "*", 57 : "C", 58 : "W", 59 : "C",
              60 : "L", 61 : "F", 62 : "L", 63 : "F", 
              }

def ProteinTranslation(RNA):
    ansStr = ""

    for x in range(0,len(RNA),3):
        pattern = RNA[x:x+3]
        code = geneticCode[geneticNames[pattern]]
        if code != "*":
            ansStr += code

    print(ansStr)

with open("data.txt", "r") as f:
    data = f.readlines()

RNAstring = data[0].replace('\n', '')

ProteinTranslation(RNAstring)
