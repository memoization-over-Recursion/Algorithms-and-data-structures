#time complexity O( n^2 )
#space complexity O( n )
def sortStack(stack):
    if( len(stack) == 0):
        return stack

    top = stack.pop()

    sortStack(stack)

    insert( stack , top )
    return stack

def insert( stack , top ):
    if(len( stack ) == 0 or top >= stack[len( stack ) - 1 ]):
        stack.append(top)
        return

    value = stack.pop()
        
    insert(stack , top)

    stack.append(value)
    
