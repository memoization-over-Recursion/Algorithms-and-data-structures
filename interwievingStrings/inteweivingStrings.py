#time complexity O( 2^(m+n) )
#space complexity O( m+n )
def interweavingStrings(one, two, three):
    if(len(one) + len(two) != len(three)):
        return False

    return inter(one , two , three , 0 , 0)

def inter(one , two , three , i , j ):
    k = i + j
    print( str(i) + " " + str(j) + " " + str(k) )
    if(k == len(three)):
        return True

    if(i < len(one) and three[k] == one[i]):
        if( inter(one , two , three , i+1 , j ) ):
            return True 

    if(j < len(two) and three[k] == two[j]):
        return inter(one , two , three , i , j+1 )

    return False
        

    
