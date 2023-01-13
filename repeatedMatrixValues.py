# time complexity O( n )
# space complexity O( min( w , h ) )
def repeatedMatrixValues(matrix):
    valueCounts = getCountsOfPotentialValues( matrix )
    for row in range( len( matrix )):
        for col in range( len( matrix[0] )):
            val = matrix[ row ][ col ]
            cc = row
            checkAndIncrement( val , valueCounts , cc )
    for col in range( len( matrix[0] )):
        for row in range( len( matrix )):
            val = matrix[ row ][ col ]
            cc = len( matrix ) + col 
            checkAndIncrement( val , valueCounts , cc )

    final = []
    for values in valueCounts:
        if valueCounts[values] == len(matrix) + len( matrix[0] ):
            final.append(values)

    return final
    



def getCountsOfPotentialValues( matrix ):
    valueCounts = {}
    smaller = matrix[0]
    if len( matrix ) < len( matrix[0] ):
        smaller = map( lambda row : row[0] , matrix )


    for val in smaller:
        valueCounts[ val ] = 0

    return valueCounts

def checkAndIncrement( val , valueCounts , cc ):
    if val not in valueCounts:
        return 
    if valueCounts[val] != cc:
        return 
    valueCounts[val] += 1