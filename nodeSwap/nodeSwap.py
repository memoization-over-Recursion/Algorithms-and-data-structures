# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

#time complexity O( n )
#spacee complexity O( 1 )
def nodeSwap(head):
    tNode = LinkedList(0)
    tNode.next = head

    prev = tNode
    while prev.next is not None and prev.next.next is not None:
        first = prev.next
        second = prev.next.next

        first.next = second.next
        second.next = first
        prev.next = second

        prev = first
    return tNode.next
