# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# time complexity O( n )
# sapce complexity O( 1 )
def linkedListPalindrome(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    reversedHalf = reverseLinkedList(slow)
    fast = head
    while reversedHalf is not None:
        if fast.value != reversedHalf.value:
            return False
        fast = fast.next
        reversedHalf = reversedHalf.next
    
    return True
    

def reverseLinkedList(head):
        prev = None
        curr = head
        while curr is not None:
            next = curr.next #points to next values in the lis
            curr.next = prev
            prev = curr
            curr = next
        return prev
    
 