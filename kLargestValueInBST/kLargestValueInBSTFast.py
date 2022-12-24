# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self , numOfNodesVisited , latestVisited):
        self.numOfNodesVisited = numOfNodesVisited
        self.latestVisited = latestVisited
# time complexity O( h + k )
# space complexity O( h )
def findKthLargestValueInBst(tree, k):
    tInfo = TreeInfo( 0 , -1 )
    reverseInOrderTraversal(tree , k , tInfo )
    
    return tInfo.latestVisited

def reverseInOrderTraversal(tree , k , tInfo ):
    if tree is None or tInfo.numOfNodesVisited >= k:
        return

    reverseInOrderTraversal(tree.right , k , tInfo )
    if tInfo.numOfNodesVisited < k:
       tInfo.numOfNodesVisited += 1
       tInfo.latestVisited = tree.value
       reverseInOrderTraversal(tree.left , k , tInfo )

    
