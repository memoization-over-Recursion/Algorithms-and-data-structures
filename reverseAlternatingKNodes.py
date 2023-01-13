# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# time complexity O( n )
# space complexity O( 1 )
def reverseAlternatingKNodes(head, k):
    final = None
    prev = None
    curr = head
    while curr is not None:
        reversed , nxt = reverseKNode(  k , curr )
        curr.next = nxt
        curr = nxt

        if prev is None:
            final = reversed
        else:
            prev.next = reversed

        count2 = 0
        while curr is not None and count2 < k:
            prev = curr
            curr = curr.next
            count2 += 1

    return final


def reverseKNode( k , head ):
    count = 0
    current = head
    prev = None
    while current is not None and count < k:
        next = current.next
        current.next = prev
        prev = current
        current = next
        count += 1
    return ( prev , current )