#time complexity O( w * n * log( n ) + n * w * log( w ) )
#space complexity O( wn )
def groupAnagrams(words):
    if(len(words) == 0):
        return []

    sortedWords = ["".join(sorted(word)) for word in words]
    indices = [i for i in range(len(words))]
    indices.sort(key = lambda word: sortedWords[word])

    result = []
    currentAnagramGroup = []
    currentWord = sortedWords[indices[0]]

    for index in indices:
        word = words[index]
        sortedWord = sortedWords[index]

        if(sortedWord == currentWord):
            currentAnagramGroup.append(word)
            continue

        result.append(currentAnagramGroup)
        currentAnagramGroup = [word]
        currentWord = sortedWord
        
    result.append(currentAnagramGroup)
    return result
