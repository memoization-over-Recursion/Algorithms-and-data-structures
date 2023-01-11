LETTER_DIGITS = {
    "a":"2",
    "b":"2",
    "c":"2",
    "d":"3",
    "e":"3",
    "f":"3",
    "g":"4",
    "h":"4",
    "i":"4",
    "j":"5",
    "k":"5",
    "l":"5",
    "m":"6",
    "n":"6",
    "o":"6",
    "p":"7",
    "q":"7",
    "r":"7",
    "s":"7",
    "t":"8",
    "u":"8",
    "v":"8",
    "w":"9",
    "x":"9",
    "y":"9",
    "z":"9",
}
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
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

    #time complexity O( n )
    #space complexity O( 1 )
    def contains(self, string):
        node = self.root
        for chars in string:
            if chars  not in node:
                return False
            node = node[chars]
        return True