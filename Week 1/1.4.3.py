# Reverse Complement Problem: Find the reverse complement of a DNA string.
# Input:  A DNA string Pattern
#Return a 3' reversed complement of a DNA string
Pattern= "AAAACCCGGT"
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):   
    # your code here
    Pattern=Reverse(Pattern)
    Pattern= Complement(Pattern)
    return Pattern
# Copy your Reverse() function here.
def Reverse(Pattern):
    # your code here
    rev= ""
    for i in reversed(Pattern):
        rev += str(i)
    return rev
# Copy your Complement() function here.
def Complement(Pattern):
    # your code here
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