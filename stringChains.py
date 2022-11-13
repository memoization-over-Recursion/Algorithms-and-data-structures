#time complexity O( n * m^2 +nlog(n) )
#space complexity O( mn )
def longestStringChain(strings):
    stringChains = {}
    for string in strings:
        stringChains[string] = {"start" : "" , "length" : 1}
    sortedStrings = sorted(strings , key = len)
    for string in sortedStrings:
        findStringChains(string , stringChains)
    print(stringChains)
    return build(strings , stringChains)

def findStringChains(string , stringChains):
    for i in range(len(string)):
        smaller = string[0:i] + string[i+1:]
        if(smaller not in stringChains):
            continue
        update(string , smaller , stringChains)
        
def update(string , smaller , stringChains):
    current = stringChains[string]["length"]
    smallerLen = stringChains[smaller]["length"]

    if(smallerLen + 1 >= current):
        stringChains[string]["length"] = smallerLen + 1
        stringChains[string]["start"] = smaller

def build(strings , stringChain):
    maxChain = 0
    chainStart = ""
    for string in strings:
        if(stringChain[string]["length"] > maxChain):
            maxChain = stringChain[string]["length"]
            chainStart = string
    if(maxChain == 1):
        return []
    longest = []
    current = chainStart
    while(current != ""):
        longest.append(current)
        current = stringChain[current]["start"]
    return longest
        

        
