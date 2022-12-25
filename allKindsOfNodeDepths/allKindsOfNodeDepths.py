# time complexity O( nlog( n ) )
# space complexity O( n )
def allKindsOfNodeDepths(root):
   if root is None:
       return 0

   return allKindsOfNodeDepths(root.left) + allKindsOfNodeDepths(root.right) + nodeDepths(root)
    
def nodeDepths( root , depth = 0 ):
    if root is None:
        return 0

    return depth + nodeDepths( root.left , depth + 1 ) + nodeDepths( root.right , depth + 1 )

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
