#time complexity O( n )
#space complexity O( 1 )
def find_missing(input):
    runningSum = 0
    for i in input:
        runningSum += i
    print(runningSum)
    leng = len(input)+1
    return leng*(leng+1)//2 - runningSum
    