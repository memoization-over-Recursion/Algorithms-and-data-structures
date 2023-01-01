# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# time complexity O( n + m )
# space compleexity O( h1 + h2 )
def compareLeafTraversal(tree1, tree2):
    stack1 = [tree1] 
    stack2 = [tree2]

    while len(stack1) > 0 and len(stack2) > 0:
        leaf1 = getLeaf(stack1)
        leaf2 = getLeaf(stack2)

        if leaf1.value != leaf2.value:
            return False

        
    return len(stack1) == 0 and len(stack2) == 0 

def getLeaf(treeStack):
    treeNode = treeStack.pop()
    while not isLeafNode(treeNode):
        if treeNode.right is not None:
            treeStack.append( treeNode.right )

        if treeNode.left is not None:
            treeStack.append( treeNode.left )
            
        treeNode = treeStack.pop()
    return treeNode

def isLeafNode(tree):
    return tree.left is None and tree.right is None
