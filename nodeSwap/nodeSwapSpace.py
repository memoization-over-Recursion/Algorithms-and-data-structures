# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

#time complexity O( n ) 
#space complexity O( n )
def nodeSwap(head):
    if head is None or head.next is None:
        return head

    nN = head.next
    head.next = nodeSwap(head.next.next)
    nN.next = head
    
    return nN
