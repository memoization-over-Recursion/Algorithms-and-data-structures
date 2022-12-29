# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# time complexity O( n^2 )
# space complexity O( n )
def reconstructBst(preOrderTraversalValues):
    if len( preOrderTraversalValues ) == 0:
        return None

    current = preOrderTraversalValues[0]
    rightIdx = len( preOrderTraversalValues )

    for i in range( 1 ,  len( preOrderTraversalValues ) ):
        val = preOrderTraversalValues[i]
        if val >= current:
            rightIdx = i
            break

    left = reconstructBst(preOrderTraversalValues[1:rightIdx])
    right = reconstructBst(preOrderTraversalValues[rightIdx : ])
    return BST(current , left , right) 