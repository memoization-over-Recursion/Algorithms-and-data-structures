#time complexity O( n )
#space complexity O( n )
def largestRectangleUnderSkyline(buildings):
    stack = []
    maxim = 0
    buildings = buildings + [0]
    for i in range( len( buildings ) ):
        while(len(stack) > 0 and buildings[stack[len(stack)-1]] >= buildings[i]):
            pillar = buildings[stack.pop()]
            ranger = i if len(stack) == 0 else i - stack[-1] - 1
            maxim = max(maxim , pillar*ranger)
        stack.append( i )
    return maxim
