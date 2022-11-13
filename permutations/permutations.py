#time complexity O( n * n! )
#space complexity O( n * n! )
def getPermutations(array):
    permut = []
    permutations(array ,[] ,permut)
    return permut
   
def permutations( array , ar , per):
    print(ar)
    if( not len(array) and len(ar)):
        per.append(ar)
    else:
        for i in range(len(array)):
            newAr = array[:i] + array[i+1:]
            
            permutedAr = ar + [array[i]]
            permutations(newAr , permutedAr , per)
