# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
# time complexity O( d )
# space complexity O( 1 )
#check if one node is a decendent and ancestor
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
   searchOne = nodeOne
   searchTwo = nodeThree
   while True:
       
        foundTFO = searchOne is nodeThree
        foundOFT = searchTwo is nodeOne
        foundT = searchOne is nodeTwo or searchTwo is nodeTwo
        finished = searchOne is None and searchTwo is None
        if foundTFO or foundOFT or foundT or finished:
            break
        
        if searchOne is not None:
            searchOne = searchOne.left if searchOne.value > nodeTwo.value else searchOne.right
        if searchTwo is not None:
            searchTwo = searchTwo.left if searchTwo.value > nodeTwo.value else searchTwo.right

       
   foundNFO = searchOne is nodeThree or searchTwo is nodeOne
   foundNT = searchOne is nodeTwo or searchTwo is nodeTwo

   if not foundNT or foundNFO:
       return False

   return search( nodeTwo , nodeThree if searchOne is nodeTwo else nodeOne )

    

        
def search( node , tar ):
    while node is not None and node is not tar:
        node = node.left if node.value > tar.value else node.right

    return node is tar
