#time complexity O( n * n! )
#space complexity O( n * n! )
def getPermutations(array):
    permut = []
    permutations(array , 0 , permut)
    return permut

def permutations(array , c , permut):
    if( c == len(array) - 1 ):
        permut.append( array[ : ] )
    else:
        for j in range(c , len(array)):
            swap(array , c , j)
            permutations(array , c+1 , permut)
            swap(array , c , j)
    
def swap(ar , i , j):
    ar[i] , ar[j] = ar[j] , ar[i]