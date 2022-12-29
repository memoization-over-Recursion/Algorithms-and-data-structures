
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for i in range( len( string ) ):
            self.insert( i , string )

    #time complexity O( n ^ 2 )
    #space complexity O( n ^ 2 )
    def insert(self ,  i , string ):
        node = self.root
        for j in range( i , len( string ) ):
            if string[j] not in node:
                node[ string[ j ] ] = {}
            node = node[ string[ j ] ]
        node[self.endSymbol] = True 

    #time complexity O( n )
    #space complexity O( 1 )
    def contains(self, string):
        node = self.root
        for chars in string:
            if chars  not in node:
                return False
            node = node[chars]
        return self.endSymbol in node
   
