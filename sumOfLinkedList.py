# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

#time complexity O( max( m , n ) )
#space complexity O( max( m , n ) )
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # 2 - 4 - 7 - 1 - none
    # 9 - 4 - 5 - none
    node = LinkedList(0) 
    currentNode = node # 0 - 1
    carry = 0
   

    nodeOne = linkedListOne # 2 - 4 - 7 - 1 - none
    nodeTwo = linkedListTwo # 9 - 4 - 5 - none

    while nodeOne is not None or nodeTwo is not None or carry != 0:
        valOne = nodeOne.value if nodeOne is not None else 0 # 2
        valTwo = nodeTwo.value if nodeTwo is not None else 0 # 9
        currentVal = valOne + valTwo + carry # 11

        newVal = currentVal % 10 # 1
        newNode = LinkedList( newVal ) # 1
        currentNode.next = newNode # 0 - 1
        currentNode = newNode 
        

        carry = currentVal // 10 # 1
        nodeOne = nodeOne.next if nodeOne is not None else None  
        nodeTwo = nodeTwo.next if nodeTwo is not None else None 
        
    return node.next
