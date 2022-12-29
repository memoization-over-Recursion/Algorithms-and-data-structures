

class UnionFind:
    def __init__(self):
        self.parents = {}
    # time complexity O( 1 ) 
    # space complexity O( 1 )
    def createSet(self, value):
        self.parents[value] = value

    # time complexity O( n ) 
    # space complexity O( 1 )
    def find(self, value):
        if value not in self.parents:
            return None 

        current = value
        while current != self.parents[current]:
            current = self.parents[current]

        return current
    # time complexity O( n ) 
    # space complexity O( 1 )
    def union(self, valueOne, valueTwo):
        if valueOne not in self.parents or valueTwo not in self.parents:
            return

        rootOne = self.find(valueOne)
        rootTwo = self.find(valueTwo)

        self.parents[rootTwo] = rootOne

        
