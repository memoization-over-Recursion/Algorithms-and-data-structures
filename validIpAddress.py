#time complexity O( 1 )
#space complexity O( 1 )
def validIPAddresses(string):
    ans = []
    if(len(string) < 4):
       return []
    for i in range(1, min(4 , len(string))):
        ipAddresses = ["" , "" , "" , ""]
        ipAddresses[0] = string[:i]
        if(not isValid(ipAddresses[0])):
            continue

        for j in range( i + 1 , i + min ( 4 , len(string)-i ) ):
            ipAddresses[1] = string[i:j]
            if(not isValid(ipAddresses[1])):
                continue

            for k in range( j + 1 , j + min ( 4 , len(string)-j ) ):
                ipAddresses[2] = string[j:k]
                ipAddresses[3] = string[k:]

                if(isValid(ipAddresses[2]) and isValid(ipAddresses[3])):
                    ans.append(".".join(ipAddresses))
    return ans
       
           
           
def isValid(string):
    sI = int(string)
    if(sI > 255):
        return False

    return len(string) == len(str(sI))
