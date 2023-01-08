# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

#time complexity O( n )
# space complexity O( 1 )
def rearrangeLinkedList(head, k):
    smallerHead = None
    smallerTail = None
    equalHead = None
    equalTail = None
    greaterHead = None
    greaterTail = None

    
    node = head
    while node is not None:
        if node.value < k:
            smallerHead , smallerTail = grow( smallerHead , smallerTail , node )
        elif node.value > k:
            greaterHead , greaterTail = grow( greaterHead , greaterTail , node )
        else:
            equalHead , equalTail = grow( equalHead , equalTail , node )

        prev = node
        node = node.next
        prev.next = None

    fHead , fTail = connect(smallerHead , smallerTail , equalHead , equalTail )
    final , _ = connect(fHead , fTail , greaterHead , greaterTail )
    return final


def grow( head , tail , node):
    newHead = head 
    newTail = node

    if newHead is None:
        newHead = node
    if tail is not None:
        tail.next = node

    return (newHead , newTail)


def connect( h1 , t1 , h2 , t2 ):
    newH = h2 if h1 is None else h1
    newT = t1 if t2 is None else t2

    if t1 is not None:
        t1.next = h2

    return (newH , newT)
    
            
        
                