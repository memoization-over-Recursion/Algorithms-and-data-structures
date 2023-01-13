# time complexity O( n )
# space complexity O( h )
def largestBstSize(tree):
    return getTreeInfo(tree).rLB

def getTreeInfo( tree ):
    if tree is None:
        return TreeInfo( True , float("-inf") , float("inf") , 0 , 0 )


    left = getTreeInfo( tree.left )
    right = getTreeInfo( tree.right )

    treeSize = 1 + left.tS + right.tS
    sBP = tree.value > left.maV and tree.value <= right.miV
    isBST = sBP and left.iB and right.iB

    maxValue = max( tree.value , max( left.maV, right.maV ))
    minValue = min( tree.value , max( left.miV , right.miV ))

    largest = 0
    if isBST:
        largest = treeSize
    else:
        largest = max( left.rLB , right.rLB )

    return TreeInfo( isBST , maxValue , minValue , largest  , treeSize)
class TreeInfo:
    def __init__(self , iB , maV , miV , rLB , tS ):
        self.iB = iB
        self.maV = maV
        self.miV = miV
        self.rLB = rLB
        self.tS = tS

    


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
