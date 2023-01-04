# time complexity O( nm*8^s +ws )
# space complexity O( nm + ws )
def boggleBoard(board, words):
    trie = Trie()
    for word in words:
        trie.insert( word )
    final = {}
    visited = [ [False for letter in row ] for row in board ]
    for i in range( len( board ) ):
        for j in range( len( board[ i ] ) ):
            explore( i , j , board , trie.root , visited , final )
    return list(final.keys())

def explore( i , j , board , trie , visited , final ):
    if visited[i][j]:
        return 

    letter = board[i][j] 
    if letter not in trie:
        return
    visited[i][j] = True
    trie = trie[letter]
    if "*" in trie:
        final[trie["*"]] = True
    neighbours = getNeighbours( i , j , board )
    for neighbour in neighbours:
        explore(neighbour[0] , neighbour[1] , board , trie , visited , final )
    visited[i][j] = False
    
def getNeighbours( i , j , board ):
    n = []
    if i > 0 and j > 0:
        n.append([ i-1 , j-1 ])
    if i > 0 and j < len( board[0] ) - 1:
        n.append([ i-1 , j+1 ])
    if i < len( board ) - 1 and j > 0:
        n.append([ i+1 , j-1 ])
    if i < len( board ) - 1 and j < len( board[0] ) - 1:
        n.append([ i+1 , j+1 ])
    if i > 0:
        n.append([ i-1 , j ])
    if j > 0:
        n.append([ i , j-1 ])
    if i < len( board ) - 1:
        n.append([ i+1 , j ])
    if j < len( board[0] ) - 1:
        n.append([ i , j+1 ])
    return n
        





class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    #time complexity O( n ^ 2 )
    #space complexity O( n ^ 2 )
    def insert(self , string ):
        node = self.root
        for letter in string:
            if letter not in node:
                node[ letter ] = {}
            node = node[ letter ]
        node[self.endSymbol] = string 

   