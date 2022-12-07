#time complexity O( snb )
#space complexity O( s )
def multiStringSearch(bigString, smallStrings):
    return [isInBigString(string , bigString) for string in smallStrings]

def isInBigString( string , bigString ):
    for i in range( len( bigString ) ):
        if i + len( string ) > len( bigString ):
            break
        if helper( string , bigString , i ):
            return True
    return False

def helper( string , bigString , i ):
    start = i
    end = i + len( string ) - 1
    start1 = 0
    end1 = len( string ) - 1
    while start <= end:
        if bigString[start] != string[start1] or bigString[end] != string[end1]:
            return False
        start += 1
        start1 += 1
        end -= 1
        end1 -= 1
    return True

