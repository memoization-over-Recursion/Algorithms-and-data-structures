#time complexity O( n^3 )
#space complexity O( n )
def longestPalindromicSubstring(string):
    longest = ""
    for i in range(len(string)):
        for j in range(i , len(string)):
            sub = string[i : j+1]
            if(len(sub) > len(longest) and isPal(sub)):
                longest = sub
    return longest

#time complexity O( n )
#space complexity O( 1 )
def isPal(string):
    start = 0
    end = len(string)-1
    while(start < end):
        if(string[start] != string[end]):
            return False
        start += 1
        end -= 1
    return True
