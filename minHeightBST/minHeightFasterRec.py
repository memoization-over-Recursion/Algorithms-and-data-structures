#create BST
#minimize height of BST
#time complexity O( n ) bcos it doesnt use inser method
#space complexity O( n )
def minHeightBst(array):
    return constructBST(array , 0 , len( array ) - 1)


def constructBST(array , left , right):
    if left > right:
        return None

    middle = ( right + left ) // 2
    bst = BST( array[ middle ] )

    bst.left = constructBST(array , left , middle - 1 )
    bst.right = constructBST(array , middle + 1 , right)

    return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
