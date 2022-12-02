#time complexity O( low * high * n )
#space complexity O( low * high )
def ambiguousMeasurements(measuringCups, low, high):
    meme = {}
    return canMeasureInRange( measuringCups , low , high , meme )


def canMeasureInRange( measuringCups , low , high , meme ):
    memeKey = createHashKey( low , high )
    if memeKey in meme:
        return meme[memeKey]

    if low <= 0 and high <= 0:
        return False

    canMeasure = False
    for cup in measuringCups:
        cupLow , cupHigh = cup
        if( low <= cupLow and cupHigh <= high ):
            canMeasure = True
            break
        newLow = max( 0 , low - cupLow)
        newHigh = max( 0 , high - cupHigh)
        canMeasure = canMeasureInRange(measuringCups , newLow , newHigh , meme)
        if canMeasure:
            break
    meme[memeKey] = canMeasure
    return canMeasure

    


def createHashKey( low , high ):
    return str(low) + ":" + str(high)
    