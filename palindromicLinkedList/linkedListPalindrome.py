# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# time complexity O( n )
# sapce complexity O( n )
def linkedListPalindrome(head):
    infoOfLinkedList = isPalindrome( head , head )
    return infoOfLinkedList.isEqual

def isPalindrome( head , head1 ):
    if head1 is None:
        return LinkedListInfo( head , True )

    recursiveCall = isPalindrome(head , head1.next )
    leftNode = recursiveCall.left
    isEquals = recursiveCall.isEqual

    isEqualRec = isEquals and leftNode.value == head1.value
    newLeft = leftNode.next

    return LinkedListInfo( newLeft , isEqualRec )
    



class LinkedListInfo:
    def __init__(self, left , isEqual):
        self.left = left
        self.isEqual = isEqual
