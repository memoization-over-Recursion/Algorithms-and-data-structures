# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# time complexity O( n )
# space complexity O( 1 )
def zipLinkedList(linkedList):
    firstHalf = linkedList
    secondHalf = splitLinkedList( linkedList )
    reverseSecondHalf = reverseLinkedList( secondHalf )
    return interweaveLinkedList( firstHalf , reverseSecondHalf )

def splitLinkedList( linkedList1 ):
    slow = linkedList1
    fast = linkedList1
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    result = slow.next
    slow.next = None
    return result

def reverseLinkedList( linkedList ):
    prev , current = None , linkedList
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

def interweaveLinkedList( lL1 , lL2 ):
    link1 = lL1
    link2 = lL2
    while link1 is not None and link2 is not None:
        link11 = link1.next
        link21 = link2.next

        link1.next = link2
        link2.next = link11

        link1 = link11
        link2 = link21

    return lL1
    