# Avg time complexity O( nlog( n ) )
# Avg space complexity O( n )
# Worst time complexity O( n^2 )
# Worst space complexity O( n )
def rightSmallerThan(array):
    if len( array ) == 0:
        return []

    rightSmaller = array[:] #clone the original array
    last = len(array) - 1 
    bst = BST(array[last])
    rightSmaller[last] = 0
    for i in reversed( range( len(array) - 1 ) ):
        bst.insert(array[i] , i , rightSmaller)

    return rightSmaller


class BST:
    def __init__( self, value ):
        self.value = value
        self.leftSubSize = 0
        self.left = None
        self.right = None
        
    def insert(self, value , id , countOnRight , numSmallerAtInsert = 0):
        if value < self.value:
            self.leftSubSize += 1
            if self.left is None:
                self.left = BST( value )
                countOnRight[id] = numSmallerAtInsert
            else:
                self.left.insert(value , id , countOnRight , numSmallerAtInsert)
        else:
            numSmallerAtInsert += self.leftSubSize
            if value > self.value:
                numSmallerAtInsert += 1
            if self.right is None:
                self.right = BST(value)
                countOnRight[id] = numSmallerAtInsert
            else:
                self.right.insert(value , id , countOnRight , numSmallerAtInsert)
        

    