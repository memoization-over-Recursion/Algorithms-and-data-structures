# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

#time complexity O( n )
#space complexity O( 1 )
def reverseLinkedList(head):
    prev = None
    curr = head
    while curr is not None:
        next = curr.next #points to next values in the list
        curr.next = prev
        prev = curr
        curr = next
    
    return prev
