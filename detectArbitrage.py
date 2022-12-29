import math
# time complexity O( n^3 )
# space complexity O( n^2 )
def detectArbitrage(exchangeRates):
    changedMatrix = convertMatrix( exchangeRates )
    
    return checkNegativeEdge( changedMatrix , 0 )

def checkNegativeEdge( edges , start ):
    disFromStart = [float("inf") for _ in range(len(edges))]
    disFromStart[start] = 0 

    for _ in range( len( edges ) - 1 ):
        if not relaxAndUpdate(edges , disFromStart):
            return False

    return relaxAndUpdate(edges , disFromStart)

def relaxAndUpdate( graph , dis ):
    updated = False
    for i , edges in enumerate(graph):
        for j , weight in enumerate(edges):
            newDis = dis[i] + weight
            if newDis < dis[j]:
                updated = True
                dis[j] = newDis
    return updated
    

def convertMatrix( er ):
    newEr = []
    for row , rates in enumerate(er):
        newEr.append([])
        for rate in rates:
            newEr[row].append(-math.log10(rate))

    return newEr