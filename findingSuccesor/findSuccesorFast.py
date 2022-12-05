# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

#time complexity O( h )
#space complexity O( 1 )
def findSuccessor(tree, node):
   if node.right is not None:
       return getLeftOnRightSub(node.right)

   return goRightParentSubTree(node)

def getLeftOnRightSub(tree):
    current = tree
    while( current.left is not None ):
        current = current.left

    return current

def goRightParentSubTree(tree):
    current = tree
    while current.parent is not None and current.parent.right == current:
        current = current.parent

    return current.parent
