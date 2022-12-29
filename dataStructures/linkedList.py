
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None



class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    #time complexity O( 1 )
    #space complexity O( 1 )
    def setHead(self, node):
        if self.head is None:
            self.head = node # this would be like a single valued linkedlist 
            self.tail = node
            return
        else:
            self.insertBefore(self.head , node)
    #time complexity O( 1 )
    #space complexity O( 1 )
    def setTail(self, node):
         if self.tail is None:
            self.setHead(node)
            return
         else:
            self.insertAfter(self.tail , node)
    #time complexity O( 1 )
    #space complexity O( 1 )
    def insertBefore(self, node, nodeToInsert):
        if self.head == nodeToInsert and self.tail == nodeToInsert:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert
    #time complexity O( 1 )
    #space complexity O( 1 )
    def insertAfter(self, node, nodeToInsert):
        if self.head == nodeToInsert and self.tail == nodeToInsert:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert
    #time complexity O( p )
    #space complexity O( 1 )
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        currentPos = 1
        while node is not None and currentPos != position:
            node = node.next
            currentPos += 1
        if node is not None:
            self.insertBefore(node , nodeToInsert)
        else:
            self.setTail(nodeToInsert)
    #time complexity O( n )
    #space complexity O( 1 )
    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)
        
    #time complexity O( 1 )
    #space complexity O( 1 )
    def remove(self, node):
        if(node == self.head):
            self.head = self.head.next
        if(node == self.tail):
            self.tail = self.tail.prev
        self.removeBindings(node)
    #time complexity O( n )
    #space complexity O( 1 )
    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None
    #time complexity O( 1 )
    #space complexity O( 1 )
    def removeBindings(self , node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None
            
