# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# time complexity O( n + m )
# space compleexity O( (n+1)/2 + (m+1)/2 )
def compareLeafTraversal(tree1, tree2):
    leaves1 = []
    leaves2 = []
    trav1 = preOrder(tree1 , leaves1)
    trav2 = preOrder(tree2 , leaves2)
    for i in range( min( len( trav1 ) , len( trav2 ) ) ):
        if trav1[i] != trav2[i]:
            return False
    return True
    
def preOrder( tree , traversal ):
    if tree is None:
        return traversal

    if isLeafNode( tree ):
        traversal.append( tree.value )
    preOrder(tree.left , traversal)
    preOrder(tree.right , traversal)

    return traversal


def isLeafNode(tree):
    return tree.left is None and tree.right is None