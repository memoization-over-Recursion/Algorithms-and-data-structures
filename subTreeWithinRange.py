# time complexity O( n )
# space complexity O( h )
def subtreesWithinRange(tree, targetRange):
    ans = {"res": 0}
    isWithinRange( tree , targetRange , ans )
    return ans["res"]
    pass

def isWithinRange( tree , target , answer ):
    if tree is None:
        return True

    leftWithinRange = isWithinRange( tree.left , target , answer)
    rightWithinRange = isWithinRange( tree.right , target , answer)
    isWithinR = tree.value >= target[0] and tree.value <= target[1]
    an = leftWithinRange and rightWithinRange and isWithinR
    if an:
        answer['res'] += 1
    return an
# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
