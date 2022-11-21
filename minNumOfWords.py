#time complexity O( n * l )
#space complexity O( c )
def minimumCharactersForWords(words):
    results = {}
    for word in words:
        wordFreq = countFreq(word)
        update( wordFreq , results )

    letters = []
    for elem in results:
        freq = results[elem]
        for _ in range( freq ):
          letters.append(elem)  

    return letters


def update( freqWord , maxFreq ):
    for freq in freqWord:
        current = freqWord[freq]
        if(freq in maxFreq):
            maxFreq[freq] = max( maxFreq[freq] , current )
        else:
            maxFreq[freq] = current
    



def countFreq(word):
    freq = {}
    for char in word:
        if( char in freq ):
            freq[char] += 1
        else:
            freq[char] = 1

    return freq
        
