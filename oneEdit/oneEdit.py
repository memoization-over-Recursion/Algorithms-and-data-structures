#time complexity O( n + m )
#space complexity O( n + m )
def oneEdit(stringOne, stringTwo):
    lenOne , lenTwo = len(stringOne) , len(stringTwo)
    if( abs(lenOne - lenTwo ) > 1 ):
        return False



    for i in range( min( lenOne , lenTwo ) ):
        if stringOne[i] != stringTwo[i]:
            if lenOne > lenTwo:
                return stringOne[ i + 1 : ] == stringTwo[ i : ]
            elif lenOne < lenTwo:
                return stringOne[ i : ] == stringTwo[ i + 1 : ]
            else:
                return stringOne[ i + 1 : ] == stringTwo[ i + 1 : ]
                
            
    return True
