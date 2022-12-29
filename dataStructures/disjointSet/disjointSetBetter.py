
class UnionFind:
    def __init__(self):
        self.parents = {}
        self.ranks = {}
    # time complexity O( 1 ) 
    # space complexity O( 1 )
    def createSet(self, value):
        self.parents[value] = value
        self.ranks[value] = 0

    # time complexity O( 1 ) 
    # space complexity O( 1 )
    def find(self, value):
        if value not in self.parents:
            return None 

        if value != self.parents[value]:
            self.parents[value] = self.find(self.parents[value])

        return self.parents[value]
            
    # time complexity O( 1 ) 
    # space complexity O( 1 )
    def union(self, valueOne, valueTwo):
        if valueOne not in self.parents or valueTwo not in self.parents:
            return

        rootOne = self.find(valueOne)
        rootTwo = self.find(valueTwo)
        if self.ranks[rootOne] < self.ranks[rootTwo]:
            self.parents[rootOne] = rootTwo
        elif self.ranks[rootOne] > self.ranks[rootTwo]:
            self.parents[rootTwo] = rootOne
        else:
            self.parents[rootTwo] = rootOne
            self.ranks[rootOne] += 1

        
