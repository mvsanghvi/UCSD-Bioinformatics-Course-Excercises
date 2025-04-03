#Output the complement of a DNA string
# Input:  A DNA string Pattern
Pattern = "AAAACCCGGT"
# Output: The complementary string of Pattern (with every nucleotide replaced by its complement).
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