#time complexity O( n^4 )
#space complexity O( 1 )
def squareOfZeroes(matrix):
    #spuare shape only 1s and 0s
    #returns a boolean to tell if matrix has square of 0s
    #0 0 0 0 0 min 2x2
    #0       0
    #0       0
    #0       0
    #0 0 0 0 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            lenOfSquare = 2
            while(lenOfSquare <= len(matrix) - row and lenOfSquare <= len(matrix) - col):
                row2 = row + lenOfSquare - 1
                col2 = col + lenOfSquare - 1
                if(isSquareOfZeros(matrix , col , row , col2 , row2)):
                    return True
                lenOfSquare += 1
    return False
            
            
            

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
        
        
        
