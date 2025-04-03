# Pattern Matching Problem: Find all occurrences of a pattern in a string.
#      Input: Strings Pattern and Genome.
#      Output: All starting positions in Genome where Pattern appears as a substring.

Pattern= 'ATAT'
Genome = 'GATATATGCATATACTT'
def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)
    # your code here
    return positions