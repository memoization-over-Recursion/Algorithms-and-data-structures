# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self , root):
        self.root = root

# time complexity O( n )
# space complexity O( n )
def reconstructBst(preOrderTraversalValues):
    treeI = TreeInfo( 0 )
    return reconstructFromRange(float("-inf") , float("inf") , preOrderTraversalValues , treeI)

def reconstructFromRange( min , max , ar , treeI):
    if treeI.root == len(ar):
        return None

    rootVal = ar[treeI.root]
    if rootVal < min or rootVal >= max:
        return None

    
    treeI.root += 1
    left = reconstructFromRange( min , rootVal , ar , treeI)
    right = reconstructFromRange( rootVal , max , ar , treeI)
    return BST(rootVal , left , right)