#time complexity O( n^2 )
#space complexity O( n )
def longestPalindromicSubstring(string):
    longestCurrent = [0,1]
    for i in range( 1 , len(string)):
        odd = findLongestPal(string , i-1 , i+1)
        even = findLongestPal(string , i-1 , i)
        longest = max(odd ,even , key = lambda x : x[1] - x[0])
        longestCurrent = max(longestCurrent , longest , key = lambda x : x[1] - x[0])
    return string[longestCurrent[0] : longestCurrent[1]]

def findLongestPal(string , left , right):
    while(left >= 0 and right < len(string)):
        if(string[left] != string[right]):
            break
        else:
            left-=1
            right+=1
    return [left+1 , right]
        
