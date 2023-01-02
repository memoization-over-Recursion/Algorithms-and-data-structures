# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# time complexity O( n )
# space complexity O( 1 )   
def shiftLinkedList(head, k):
    listLength = 1
    tail = head
    while tail.next is not None:
        tail = tail.next
        listLength += 1
    offset = abs(k) % listLength
    if offset == 0:
        return head

    curPos = listLength - offset if k > 0 else offset
    tail2 = head
    for i in range(1 , curPos):
        tail2 = tail2.next

    tail3 = tail2.next
    tail2.next = None
    tail.next = head
    return tail3
        
    
    