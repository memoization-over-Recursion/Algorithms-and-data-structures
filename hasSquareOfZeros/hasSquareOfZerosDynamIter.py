#time complexity O( n^3 )
#space complexity O( n^2 )
def squareOfZeroes(matrix):
    #spuare shape only 1s and 0s
    #returns a boolean to tell if matrix has square of 0s
    #0 0 0 0 0 min 2x2
    #0       0
    #0       0
    #0       0
    #0 0 0 0 0
   matrixo = preComputeNum(matrix)
   for row in range(len(matrixo)):
        for col in range(len(matrixo[0])):
            lenOfSquare = 2
            while(lenOfSquare <= len(matrixo) - row and lenOfSquare <= len(matrixo) - col):
                row2 = row + lenOfSquare - 1
                col2 = col + lenOfSquare - 1
                if(isSquareOfZeros(matrixo , col , row , col2 , row2)):
                    return True
                lenOfSquare += 1
   return False

def isSquareOfZeros(matrix , c1 , r1 , c2 , r2):
    squareLength = c2-c1 + 1
    belowTopLeft = matrix[r1][c1]["zeroBelow"] >= squareLength
    rightTopLeft = matrix[r1][c1]["zeroRight"] >= squareLength
    rightBottomLeft = matrix[r2][c1]["zeroRight"] >= squareLength
    belowTopRight = matrix[r1][c2]["zeroBelow"] >= squareLength
    return belowTopLeft and rightTopLeft and rightBottomLeft and belowTopRight
    
def preComputeNum(matrix):
    infoMatrix = [[x for x  in y] for y in matrix]
    length = len(matrix)
    for row in range(length):
        for col in range(length):
            numOfZeros =  1 if matrix[row][col] == 0 else 0
            infoMatrix[row][col] = {
                "zeroBelow" : numOfZeros,
                "zeroRight" : numOfZeros,
            }
    id = len(matrix) - 1
    for row in reversed(range(length)):
        for col in reversed(range(length)):
            if(matrix[row][col] == 1):
                continue
            else:
                if(row < id):
                    infoMatrix[row][col]["zeroBelow"] += infoMatrix[row+1][col]["zeroBelow"]
                if(col < id):
                    infoMatrix[row][col]["zeroRight"] += infoMatrix[row][col+1]["zeroRight"]
    return infoMatrix

            
            


