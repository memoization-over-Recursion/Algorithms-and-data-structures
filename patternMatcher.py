#time complexity O( n^2 + m )
#space complexity O( n + m )
def patternMatcher(pattern, string):
    if( len( string ) < len( pattern ) ):
        return []
    newPattern = changePattern(pattern)
    switched = newPattern[0] != pattern[0]
    counts = [ 0 , 0 ] # counts of x and y
    firstY = getPatternCount(newPattern , counts )
    if(counts[1] != 0 ):
        for lenOfX in range( 1 , len ( string ) ):
            lenOfY = (len( string ) - lenOfX * counts[0] ) // counts[1]
            if(lenOfY <= 0 or lenOfY % 1 != 0):
                continue
            lenOfY = int(lenOfY)
            idOfY = firstY * lenOfX
            
            x = string[:lenOfX]
            y = string[idOfY : (idOfY + lenOfY)]
            
            potential = map( lambda char: x if char == 'x' else y , newPattern )
            if("".join(potential) == string):
                return [ x , y ] if not switched else [ y , x ]
    else:
        lenOfX = len(string) / counts[0]
        if(lenOfX % 1 == 0):
            lenOfX = int(lenOfX)
            x = string[:lenOfX]
            potential = map( lambda char : x if char == "x" else "" , newPattern)
            if("".join(potential) == string):
                return [ x , "" ] if not switched else [ "" , x ] 
    return []
    #yId = firstY * len( x  string )
    #len y = ( len string - x * counts[0] ) // counts[1]
        




def getPatternCount( pattern , xAndY ):
    foundFirstY = False
    firstY = -1 
    
    for i in range( len( pattern ) ):
        if(not foundFirstY):
            if(pattern[i] == 'y'):
                firstY = i
                xAndY[1] += 1
                foundFirstY = True
            else:
                xAndY[0] += 1
        else:
            if(pattern[i] == 'x'):
                xAndY[0] += 1
            else:
                xAndY[1] += 1
    return firstY
            

def changePattern( pattern ):
    newPattern = []
    if pattern[0] == 'x':
        return list(pattern)
    for char in pattern:
        if char == 'y':
            newPattern.append('x')
        else:
            newPattern.append('y')
    return newPattern