# Input:  A string Pattern
Pattern="AAAACCCGGT"
# Output: The reverse of Pattern
def Reverse(Pattern):
    # your code here
    rev= ""
    for i in reversed(Pattern):
        rev += str(i)
    return rev