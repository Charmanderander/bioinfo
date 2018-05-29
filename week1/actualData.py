import re

# fill in your PatternMatching() function along with any subroutines that you need.
def PatternMatching(Pattern, Genome):
    return [m.start() for m in re.finditer(r'(?=('+Pattern+'))',Genome)]

def Reader():
    with open("Vibrio_cholerae", "r") as f:
        text = f.read()
    return text

text = Reader()
print PatternMatching("CTTGATCAT", text)
