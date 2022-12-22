# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

#time complexity O( n ) 
#space complexity O( 1 )
def findLoop(head):
    fast = head.next.next
    slow = head.next
    while fast != slow:
        fast = fast.next.next
        slow = slow.next
    slow = head
    while fast != slow:
        fast = fast.next
        slow = slow.next
    return slow
