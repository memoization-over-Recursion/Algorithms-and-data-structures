# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# time complexity O( n + m )
# space compleexity O( max( h1, h2 ) )
def compareLeafTraversal(tree1, tree2):
    stack1 , _ = getLeaf(tree1)
    stack2 , _ = getLeaf(tree2)


    leaf1 = stack1
    leaf2 = stack2
    while leaf1 is not None and leaf2 is not None:
        

        if leaf1.value != leaf2.value:
            return False

        leaf1 = leaf1.right
        leaf2 = leaf2.right

    return leaf1 is None and leaf2 is None
        

def getLeaf(cur , head = None , prev = None ):
    if cur is None:
        return head , prev

    if isLeafNode(cur):
        if prev is None:
            head = cur
        else:
            prev.right = cur

        prev = cur
    left1 , left2 = getLeaf(cur.left , head , prev)
    return getLeaf(cur.right , left1 , left2)

        
    

def isLeafNode(tree):
    return tree.left is None and tree.right is None
