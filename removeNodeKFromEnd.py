# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

#time complexity O( n )
#space complexity O( 1 )
def removeKthNodeFromEnd(head, k):

    first = head
    second = head
    pos = 1
    while pos <= k:
        second = second.next
        pos += 1
    print(head.value)
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return
        
    while second.next is not None:
        first = first.next
        second = second.next
    print(head.value)  
    first.next = first.next.next

