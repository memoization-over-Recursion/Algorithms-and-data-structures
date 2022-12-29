# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

#time complexity O( m + n )
#space complexity O( 1 )
def mergingLinkedLists(linkedListOne, linkedListTwo):
    currentOne = linkedListOne
    currentTwo = linkedListTwo

    while currentOne is not currentTwo:
        if not currentOne:
            currentOne = linkedListTwo
        else:
            currentOne = currentOne.next

        if not currentTwo:
            currentTwo = linkedListOne
        else:
            currentTwo = currentTwo.next
        
    return currentOne