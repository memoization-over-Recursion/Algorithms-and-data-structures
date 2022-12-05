# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

#time complexity O( n )
#space complexity O( n )
def findSuccessor(tree, node):
    ar = []
    inOrder(tree , ar)
    for i in range( len(ar) - 1 ):
        if(ar[i] != node):
            continue
        
        if( i == len( ar ) - 1):
            return None
            
        return ar[i+1]

def inOrder(tree , ar ):
    if(tree == None):
        return ar

    inOrder(tree.left , ar)
    ar.append(tree)
    inOrder(tree.right , ar)

    return ar
