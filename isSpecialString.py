# time complexity O( n * m )
# space complexity O( n * m )
def specialStrings(strings):
    trie = Trie()
    for string in strings:
        trie.insert(string)
    return list(filter(lambda s : isSpecial( s , trie.root , 0 , 0 , trie)  , strings))
    pass

def isSpecial( s , trieNode , idx , c , trie ):
    char = s[idx]
    if char not in trieNode:
        return False


    endOfString = idx == len(s) - 1
    if endOfString:
        return trie.endSymbol in trieNode[char] and c + 1 >= 2

    if trie.endSymbol in trieNode[char]:
        restIsSpecial = isSpecial( s , trie.root , idx+1 , c+1 , trie )
        if restIsSpecial:
            return True

    return isSpecial( s , trieNode[char] , idx + 1 , c , trie)
    
class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    #time complexity O( n ^ 2 )
    #space complexity O( n ^ 2 )
    def insert(self , string ):
        node = self.root
        for j in range( len( string ) ):
            if string[j] not in node:
                node[ string[ j ] ] = {}
            node = node[ string[ j ] ]
        node[self.endSymbol] = True 
