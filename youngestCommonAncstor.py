# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

# time complexity O( d )
# space complexity O( 1 )
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    d1 = getDepths(topAncestor , descendantOne)
    d2 = getDepths(topAncestor , descendantTwo)
    if d1 > d2:
        return backtrack( descendantOne, descendantTwo , d1 - d2)
    else:
        return backtrack( descendantTwo , descendantOne , d2 - d1)

def getDepths( a , b ):
    result = 0
    while b != a:
        result += 1
        b = b.ancestor
    return result

def backtrack( a , b , c ):
    while c > 0:
        a = a.ancestor
        c-=1
    while a != b:
        a = a.ancestor
        b = b.ancestor
    return a