# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
# time complexity O( h )
# space complexity O( 1 )
#check if one node is a decendent and ancestor
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    if isDecendent( nodeTwo , nodeOne ):
        return isDecendent(nodeThree , nodeTwo)

    if isDecendent( nodeTwo , nodeThree ):
        return isDecendent( nodeOne , nodeTwo )
    return False

def isDecendent( node1 , node2 ):
    while node1 is not None and node1 is not node2:
        node1 = node1.left if node1.value > node2.value else node1.right

    return node1 is node2
