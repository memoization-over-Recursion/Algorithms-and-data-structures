 # This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    h1 = headOne
    h2 = headTwo
    h1prev = None
    while h1 is not None and h2 is not None:
        if h1.value < h2.value:
            h1prev = h1
            h1 = h1.next
        else:
            if h1prev is not None:
                h1prev.next = h2  
            h1prev = h2
            h2 = h2.next
            h1prev.next = h1
            print( headOne.value , "-> " , end = " " )
            
    if h1 is None:
        h1prev.next = h2
        
    return headOne if headOne.value < headTwo.value else headTwo
    
        
