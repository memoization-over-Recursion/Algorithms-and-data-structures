#time complexity O( mn )
#space complexity O( mn )
def interweavingStrings(one, two, three):
    if(len(one) + len(two) != len(three)):
        return False
    cache = [[None for i in range(len(two) + 1)] for j in range(len( one ) + 1)]
    return inter(one , two , three , 0 , 0 , cache)

def inter(one , two , three , i , j , cache ):
    if(cache[i][j] is not None):
        return cache[i][j]
    
    k = i + j
    if(k == len(three)):
        return True

    if(i < len(one) and three[k] == one[i]):
        cache[i][j] = inter(one , two , three , i+1 , j , cache )
        if(cache[i][j]):
            return True

    if(j < len(two) and three[k] == two[j]):
        cache[i][j] = inter(one , two , three , i , j+1 , cache )
        return cache[i][j]

    cache[i][j] = False
    return False
        

