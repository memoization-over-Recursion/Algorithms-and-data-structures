# time complexity O( n ) 
# space complexity O( 1 )
def iterativeInOrderTraversal(tree, callback):
    current = tree
    prev = None
    while current is not None:
        if prev is None or prev == current.parent:
            if current.left is not None:
                nextNode = current.left
            else:
                callback(current)
                nextNode = current.right if current.right is not None else current.parent
        elif prev == current.left:
            callback(current)
            nextNode = current.right if current.right is not None else current.parent  
        else:
            nextNode = current.parent
        prev = current
        current = nextNode
            
 