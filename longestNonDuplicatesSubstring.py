#time complexity O( n )
#space complexity O( min( a , n ) )
def longestSubstringWithoutDuplication(string):
    lastSeen = {}
    longest = [0,1]
    start = 0
    for i in range( len( string ) ):
        if(string[i] in lastSeen):
            start = max( start , lastSeen[string[i]] + 1 )
            
        if(longest[1] - longest[0] < i+1-start):
            longest = [start , i + 1 ]
        lastSeen[string[i]] = i

    return string[longest[0]:longest[1]]