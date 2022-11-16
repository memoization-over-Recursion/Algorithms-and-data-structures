#time complexity O( mn )
#space complexity O( mn )
def globMatching(fileName, pattern):
    table = makeTable(fileName , pattern)
    for i in range(1, len(fileName)+1):
        for j in range(1, len(pattern)+1):
            if(pattern[j-1] == "*"):
                table[i][j] = table[i][j-1] or table[i-1][j]
            elif(pattern[j-1] == "?" or pattern[j-1] == fileName[i-1]):
                table[i][j] = table[i-1][j-1]
    return table[len(fileName)][len(pattern)]

def makeTable(file , pattern):
    table = [[False for j in range( len(pattern) + 1)] for i in range(len(file)+1)]
    table[0][0] = True
    for j in range(1, len(pattern)+1):
        if(pattern[j-1] =="*"):
            table[0][j] = table[0][j-1]
    return table
                