#create BST
#minimize height of BST
#time complexity O( log( n ) )
#space complexity O( n )
def minHeightBst(array):
    return constructBST(array , None , 0 , len( array ) - 1)


def constructBST(array , bst , left , right):
    if left > right:
        return 

    middle = ( right + left ) // 2
    valToInsert = array[ middle ]

    if bst is None:
        bst = BST( valToInsert )
    else:
        bst.insert( valToInsert )

    constructBST(array , bst , left , middle - 1 )
    constructBST(array , bst , middle + 1 , right)

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
