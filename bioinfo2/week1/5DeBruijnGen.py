import sys
# put your python code here
def DeBruijn(strings):
    presufDict = {}

    for string in strings:
        presufDict[Prefix(string)] = []

    for string in strings:
        presufDict[Prefix(string)].append(Suffix(string))

    return presufDict

def Prefix(string):
    return string[:-1]

def Suffix(string):
    return string [1:]

input = sys.stdin.read().split('\n')

ans = DeBruijn(input)
for item in ans:
    print(item + " -> " + ",".join(ans[item]))
