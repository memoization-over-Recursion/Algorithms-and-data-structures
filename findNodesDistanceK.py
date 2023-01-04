# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# time complexity O( n )
# space compleexity O( n )
def findNodesDistanceK(tree, target, k):
    answer = []
    findDistanceNodeToTarget(tree , target , k , answer)
        
    return answer


def  findDistanceNodeToTarget(tree , target , k , answer ):
    if tree is None:
        return -1

    if tree.value == target:
        addSubTree(tree , 0 , k , answer )
        return 1

    left = findDistanceNodeToTarget(tree.left , target , k , answer )
    right = findDistanceNodeToTarget(tree.right , target , k , answer )

    if left == k or right == k:
        answer.append( tree.value )

    if left != -1:
        addSubTree(tree.right , left + 1 , k , answer)
        return left + 1

    if right != -1:
        addSubTree(tree.left , right + 1 , k , answer)
        return right + 1

    return -1 

def addSubTree( tree , target , k , answer):
    if tree is None:
        return 
    if target == k:
        answer.append(tree.value)
    else:
        addSubTree( tree.left , target+1 , k , answer)
        addSubTree( tree.right , target+1 , k , answer)
        
    

    
    
