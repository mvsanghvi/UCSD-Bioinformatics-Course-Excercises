Pattern = "AAAACCCGGT"
def Complement(Pattern):
    comp = ""
    for i in Pattern:
        if i == "A":
            comp += str("T")
        elif i == "C":
            comp += str("G")
        elif i == "G":
            comp += str("C")
        elif i == "T":
            comp += str("A")
    return comp