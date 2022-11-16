#time complexity O( n )
#space complexity O( n )
def shortenPath(path):
    stack = []
    filteredPath = filter(filtered , path.split("/"))
    isRoot = path[0] == '/'
    if(isRoot):
        stack.append("")
    for token in filteredPath:
        if(token == '..'):
            if(len(stack) == 0 or stack[-1] == ".."):
                stack.append(token)
            elif(stack[-1] != ""):
                stack.pop()
        else:
            stack.append(token)

    if(len(stack) == 1 and stack[0] == ""):
        return '/'
    return "/".join(stack)
    
def filtered(token):
    if(len(token) > 0 and token != '.'):
        return token
