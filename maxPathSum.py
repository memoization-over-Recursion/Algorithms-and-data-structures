#time complexity O( n )
#space complexity O( log( n ) )
def maxPathSum( tree ):
    _ , maxPath = getMaxPath( tree )
    return maxPath

def getMaxPath( tree ):
    if tree is None:
        return 0 , float( "-inf" )

    LBranch , LMax = getMaxPath( tree.left )
    RBranch , RMax = getMaxPath( tree.right )
    maxBranch = max( LBranch , RBranch )

    val = tree.value
    rootMaxBranch = max( maxBranch + val , val )
    treeMaxBranch = max( LBranch + val + RBranch , rootMaxBranch )
    maxPathSum = max(LMax, treeMaxBranch , RMax)

    return rootMaxBranch , maxPathSum
    
    