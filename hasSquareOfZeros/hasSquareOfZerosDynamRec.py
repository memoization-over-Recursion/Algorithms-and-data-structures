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
    matrixOfInfo = preComputeNum(matrix)
    last = len(matrix) - 1
    return hasSquareOfZeros(matrixOfInfo , 0 , 0 , last , last , {})


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

            
            


