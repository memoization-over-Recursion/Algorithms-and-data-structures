# time complexity O( n + m )
# space complexity O( n )
def countContainedPermutations(bigString, smallString):
    smallCounts = getCharCounts( smallString )
    uniqueCharCount = len( smallCounts.keys() )

    running = {}
    permuteCount = 0
    doneUniqueChars = 0
    left = 0
    right = 0
    while right < len( bigString ):
        rightChar = bigString[ right ]
        if rightChar in smallCounts:
            increasesCount( rightChar , running )

            if running[ rightChar ] == smallCounts[rightChar]:
                doneUniqueChars += 1

        if uniqueCharCount == doneUniqueChars:
            permuteCount += 1

        right += 1
        leftIncrement = right - left == len( smallString )
        if not leftIncrement:
            continue

        leftChar = bigString[left] 
        if leftChar in smallCounts:
            if running[ leftChar ] == smallCounts[ leftChar ]:
                doneUniqueChars -= 1
            decreaseCharCount( leftChar , running )

        left += 1

    return permuteCount


def getCharCounts( string ):
    count = {}
    for char in string:
        increasesCount( char , count )
    return count


def increasesCount( char , count ):
    if char not in count:
        count[char] = 0
    count[char] += 1

def decreaseCharCount( char , count ):
    count[char] -= 1
