#time complexity O( ns + bs )
#space complexity O( ns )
def multiStringSearch(bigString, smallStrings):
    trie = Trie(bigString)
    for string in smallStrings:
        trie.insert(string)

    conStrings = {}
    for i in range( len( bigString ) ):
        findSmallString(bigString , i , trie , conStrings)

    return [ string in conStrings for string in smallStrings]
        
        

def findSmallString(string , start , trie , conStrings):
    current = trie.root
    for i in range(start , len(string)):
        cChar = string[i]
        if(cChar not in current):
            break
        current = current[cChar]
        if trie.endSymbol in current:
            conStrings[ current[ trie.endSymbol ] ] = True
            


class Trie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"

    #time complexity O( n ^ 2 )
    #space complexity O( n ^ 2 )
    def insert(self , string ):
        node = self.root
        for j in range(len( string ) ):
            if string[j] not in node:
                node[ string[ j ] ] = {}
            node = node[ string[ j ] ]
        node[self.endSymbol] = string 

