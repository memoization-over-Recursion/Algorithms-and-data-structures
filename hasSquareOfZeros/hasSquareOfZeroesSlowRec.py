#time complexity O( n^4 )
#space complexity O( n^3 )
def squareOfZeroes(matrix):
    #spuare shape only 1s and 0s
    #returns a boolean to tell if matrix has square of 0s
    #0 0 0 0 0 min 2x2
    #0       0
    #0       0
    #0       0
    #0 0 0 0 0
    maxLength = len(matrix) - 1
    return hasSquareOfZeros(matrix , 0 , 0 , maxLength , maxLength , {})


def hasSquareOfZeros(matrix , r1 , c1 , r2 , c2 , c):
    if(r1 >= r2 or c1 >= c2):
        return False
    key = str(r1)+"-"+str(c1)+"-"+str(r2)+"-"+str(c2)
    if(key in c):
        return c[key]

    c[key] = (isSquareOfZeros(matrix , c1 , r1 , c2 , r2) 
              or hasSquareOfZeros(matrix , r1 + 1 , c1 + 1 , r2 - 1 , c2 - 1 , c)
              or hasSquareOfZeros(matrix , r1 , c1 + 1 , r2  - 1, c2 , c)
              or hasSquareOfZeros(matrix , r1 + 1 , c1 , r2 , c2 - 1 , c)
              or hasSquareOfZeros(matrix , r1 + 1 , c1 + 1 , r2 , c2 , c)
              or hasSquareOfZeros(matrix , r1 , c1 , r2 - 1 , c2 - 1 , c)
             )
    return c[key]
            
            
            

#time complexity O( n )
#space complexity O( 1 )
def isSquareOfZeros(matrix , col1 , row1 , col2 , row2):
    for i in range(col1 , col2+1):
        if(matrix[row1][i] != 0 or matrix[row2][i] != 0):
            return False
    for j in range(row1 , row2+1):
        if(matrix[j][col1] != 0 or matrix[j][col2] != 0):
            return False
    return True
        
        
        
