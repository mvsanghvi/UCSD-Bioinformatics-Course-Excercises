#Count the number of 3 nucleotide sequences in a given string

def PatternCount(Text, Pattern):
    # fill in your function here
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count += 1
    return count 