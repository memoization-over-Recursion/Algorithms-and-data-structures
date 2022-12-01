#time complexity O( m + n )
#space complexity O( n )
def underscorifySubstring(string, substring):
    collapsedLocations = collapseLocations(getLocations(string , substring))
    return underscorify( collapsedLocations , string )
    
def getLocations( string , sub ):
    l = []
    id = 0
    while id < len( string ):
        newId = string.find( sub , id )
        if newId != -1:
            l.append([ newId , newId + len( sub ) ])
            id = newId + 1
        else:
            break
    return l

def collapseLocations(locations):
    if not len ( locations ):
        return locations
    newLocations = [locations[0]]
    prevLocations = newLocations[0]
    for i in range( 1 , len( locations )):
        current = locations[i]
        if(current[0] <= prevLocations[1]):
            prevLocations[1] = current[1]
        else:
            newLocations.append(current)
            prevLocations = current
    return newLocations

def underscorify(locations , string):
    locId = 0
    stringId = 0
    inbetween = False
    answer = []
    i = 0
    while( stringId < len( string ) and locId < len( locations ) ):
        if(stringId == locations[locId][i]):
            answer.append("_")
            inbetween = not inbetween
            if not inbetween:
                locId += 1
            i = 0 if i == 1 else 1
        answer.append(string[stringId])
        stringId += 1
    if(locId < len( locations )):
        answer.append("_")
    elif(stringId < len( string ) ):
        answer.append( string[ stringId: ])
    return "".join(answer)
            

    