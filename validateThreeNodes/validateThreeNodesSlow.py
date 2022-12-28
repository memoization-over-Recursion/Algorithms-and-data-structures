# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
# time complexity O( h )
# space complexity O( h )
#check if one node is a decendent and ancestor
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    if isDecendent( nodeTwo , nodeOne ):
        return isDecendent(nodeThree , nodeTwo)

    if isDecendent( nodeTwo , nodeThree ):
        return isDecendent( nodeOne , nodeTwo )
    return False

def isDecendent( node1 , node2 ):
    if node1 is None:
        return False

    if node1 is node2:
        return True

    return isDecendent( node1.left , node2 ) if node2.value < node1.value else isDecendent( node1.right , node2 )
