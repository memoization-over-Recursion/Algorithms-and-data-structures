# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# time complexity O( n )
# space complexity O( 1 )
def invertedBisection(head):
    l = length(head)
    if l <= 3:
        return head

    firstHalf = getMiddle( head , l )
    middle = None
    secondHalf = None
    if l % 2 == 0:
        secondHalf = firstHalf.next
    else:
        middle = firstHalf.next
        secondHalf = firstHalf.next.next

    firstHalf.next = None
    reverseList(head)
    reversedSecond = reverseList(secondHalf)

    if middle is None:
        head.next = reversedSecond
    else:
        head.next = middle
        middle.next = reversedSecond

    return firstHalf
    
        
        



def getMiddle( head , length ):
    halfLength = length // 2
    current = 1
    cur = head
    while current != halfLength:
        cur = cur.next
        current += 1
    return cur

def reverseList( head ):
    cur = head
    prev = None
    while cur is not None:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev
    
def length( head ):
    l = 0
    cur = head
    while cur is not None:
        cur = cur.next
        l += 1
    return l