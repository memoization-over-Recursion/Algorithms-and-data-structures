#time complexity O( n^2 )
#space complexity O( 1 )
def largestRectangleUnderSkyline(buildings):
    maxim = 0
    for pillar in range( len( buildings ) ):
        current = buildings[pillar]
        left = pillar
        while left > 0 and buildings[left-1] >= current:
            left -= 1
        right = pillar
        while right < len(buildings)-1 and buildings[right+1] >= current:
            right += 1

        area = (right - left+1) * current
        maxim = max(maxim , area)
    return maxim
