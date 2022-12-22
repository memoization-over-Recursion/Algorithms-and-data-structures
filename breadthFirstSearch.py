# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self
    #time complexity O( v + e ) 
    #space complexity O( v )
    def breadthFirstSearch(self, array):
        q = [self]
        while len( q ) > 0# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self
    #time complexity O( v + e ) 
    #space complexity O( v )
    def breadthFirstSearch(self, array):
        q = [self]
        while len( q ) > 0:
            current = q.pop( 0 )
            array.append( current.name )
            for child in current.children:
                q.append(child)
        return array
        
        
:
            current = q.pop( 0 )
            array.append( current.name )
            for child in current.children:
                q.append(child)
        return array
        
        
