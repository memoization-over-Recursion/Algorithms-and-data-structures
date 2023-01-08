
class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.cache = {}
        self.currentSize = 0
        self. listOfMostRecent = DoublyLinkedList()
    # time complexity O( 1 )
    # space complexity O( 1 ) 
    def insertKeyValuePair(self, key, value):
        if key not in self.cache:
            if self.currentSize == self.maxSize:
                self.evictLastRecent()
            else:
                self.currentSize += 1
            self.cache[key] = Node(key , value)
        else:
            self.replaceKey(key , value)
        self.updateMostRecent(self.cache[key])
            
                
    # time complexity O( 1 )
    # space complexity O( 1 )
    def getValueFromKey(self, key):
        if key not in self.cache:
            return None
        self.updateMostRecent(self.cache[key])
        return self.cache[key].value
    # time complexity O( 1 )
    # space complexity O( 1 )
    def getMostRecentKey(self):
        if self.listOfMostRecent.head is None:
            return None
        return self.listOfMostRecent.head.key
    
    def evictLastRecent(self):
        keyToRemove = self.listOfMostRecent.tail.key
        self.listOfMostRecent.removeTail()
        del self.cache[keyToRemove]

    def updateMostRecent(self , node):
        self.listOfMostRecent.setHeadTo(node)

    def replaceKey( self , key , value ):
        if key not in self.cache:
            raise Exception("no")
        self.cache[key].value = value

class Node:
    def __init__(self,  key ,  value):
        self.value = value
        self.key = key
        self.prev = None
        self.next = None


    def removeBindings(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev

        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def removeTail(self):
        if self.tail is None:
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None
    
    def setHeadTo(self , node):
        if self.head == node:
            return
        elif self.head is None:
            self.head = node
            self.tail = node
        elif self.head == self.tail: