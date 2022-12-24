# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# time complexity O( n )
# space complexity O( n )
def findKthLargestValueInBst(tree, k):
    answer = []
    inOrder(tree , answer)
    return answer[ len(answer) - k ]

def inOrder( tree , answer ):
    if tree is None:
        return a

    inOrder( tree.left , answer )
    answer.append( tree.value )
    inOrder( tree.right , answer )

    return answer

    
