# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

#time complexity O( n )
#space complexity O( h )
def heightBalancedBinaryTree(tree):
    return abs(height(tree.left , -1 ) - height(tree.right , -1 )) <= 1

def height(tree , h):
    if(tree is None):
        return 0

    h1 = height(tree.left , h)
    h2 = height(tree.right , h)
    if(abs( h1 - h2 ) <= 1):
        h = max( height(tree.left , h ) , height(tree.right , h  ) ) + 1
    
    return h

    

    
