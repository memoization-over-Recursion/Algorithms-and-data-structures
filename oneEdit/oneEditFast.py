#time complexity O( n ) 
#space complexity O( 1 )
def oneEdit(stringOne, stringTwo):
    lenOne , lenTwo = len(stringOne) , len(stringTwo)
    if( abs(lenOne - lenTwo ) > 1 ):
        return False

    x = 0
    y = 0
    edited = False
    while x < lenOne and y < lenTwo:
        if stringOne[x] != stringTwo[y]:
            if edited:
                return False
            edited = True
            if lenOne > lenTwo:
                x += 1
            elif lenOne < lenTwo:
                y += 1
            else:
                x += 1
                y += 1

        else:
            x += 1
            y += 1
    return True
