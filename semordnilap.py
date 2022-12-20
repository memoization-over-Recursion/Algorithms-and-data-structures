#time complexity O( m * n )
#space complexity O( m * n )
def semordnilap(words):
    setOfWords = set(words)
    ans = []
    for word in words:
        reversed = word[::-1]
        if reversed in setOfWords and reversed != word:
          ans.append([word , reversed])
          setOfWords.remove(word)
          setOfWords.remove(reversed)
            
    
    return ans
