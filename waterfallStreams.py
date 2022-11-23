#time complexity O( w^2 * h )
#space complexity O( w )
def waterfallStreams(array, source):
    rowAbove = array[0][:]
    rowAbove[source] = -1
    for row in range(1, len( array ) ):
        currentRow = array[row][:]
        for id in range( len( rowAbove ) ):
            valAbove = rowAbove[id]
            waterAbove = valAbove < 0
            blockHere = currentRow[id] == 1

            if( not waterAbove ):
                continue

            if( not blockHere ):
                currentRow[id] += valAbove
                continue

            waterSplit = valAbove / 2

            leftI = id
            while leftI - 1 >= 0:
                leftI -= 1
                if(rowAbove[leftI] == 1):
                    break
                if(currentRow[leftI] != 1):
                    currentRow[leftI] += waterSplit
                    break

            rightI = id
            while rightI + 1 < len( rowAbove ):
                rightI += 1
                if(rowAbove[rightI] == 1):
                    break
                if(currentRow[rightI] != 1):
                    currentRow[rightI] += waterSplit
                    break
        rowAbove = currentRow
    

    return list(map(lambda x : x  * -100 , rowAbove))
            
            

            
        
        
    

