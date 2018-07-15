

def LinearSubPeptide(peptide):
    peptideLen = len(peptide)
    subPeptideLen = ((peptideLen * (peptideLen +1)) / 2)

    return subPeptideLen
