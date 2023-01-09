# time compleexity O( n )
# space complexity O( 1 )
def longestStreakOfAdjacentOnes(array):
    longestStreak = 0
    longestReplacedZero = -1
    currentStreak = 0
    replacedZero = -1

    for i in range( len( array ) ):
        if array[i] == 1:
            currentStreak += 1
        else:
            currentStreak = i - replacedZero
            replacedZero = i

        if currentStreak > longestStreak:
            longestStreak = currentStreak
            longestReplacedZero = replacedZero

    return longestReplacedZero
    
    
    
            
