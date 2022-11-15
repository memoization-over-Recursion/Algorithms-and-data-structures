#time complexity O( n )
#space complexity O( n )
def sunsetViews(buildings, direction):
    if(len(buildings) == 1):
        return [0]
    ans = []
    current = float('-inf')
    if( direction == 'EAST'):
        for i in range(len(buildings)-1 , -1 , -1):
            if(current < buildings[i] ):
                current = buildings[i]
                ans.append(i)
        ans = ans[::-1]
        
    
    else:
        for i in range(0 , len(buildings)):
            if(current < buildings[i] ):
                current = buildings[i]
                ans.append(i)

    return ans
        
    
