#time complexity O( log( n ) ) 
#space complexity O( 1 )
def findClosestValueInBst(tree, target):
    CLOSEST = float("inf")
    return helper(tree , target , CLOSEST)

def helper( tree , target , CLOSEST ):
    if(abs( target - tree.value ) < abs( target - CLOSEST )):
        CLOSEST = tree.value

    if(tree.value < target and tree.right != None):
        return helper(tree.right , target , CLOSEST)

    if(tree.value > target and tree.left != None):
        return helper(tree.left, target , CLOSEST)
        
    return CLOSEST


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
