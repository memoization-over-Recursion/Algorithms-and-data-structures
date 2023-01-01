# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# time complexity O( n )
# sapce complexity O( d )
def rightSiblingTree(root):
    mutateTree( root  , None  , None )
    return root


def mutateTree( root , parent , isLChild):
    if root is None:
        return
    left , right = root.left , root.right
    mutateTree( left , root , True )
    if parent is None:
        root.right = None
    elif isLChild:
        root.right = parent.right
    else:
        if parent.right is None:
            root.right = None
        else:
            print( parent.right.left )
            root.right = parent.right.left
    mutateTree( right , root , False )
            
        
    
