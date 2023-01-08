# time complexity O( v + e )
# space compleexity O( v )
def cycleInGraph(edges):
    numOfNodes = len(edges)
    visited = [False for _ in range( numOfNodes ) ]
    currentInStack = [False for _ in range( numOfNodes ) ]
    for node in range( numOfNodes ):
        if visited[node]:
            continue

        if isNodeInCycle( node , edges , visited , currentInStack):
            return True
    
    return False

def isNodeInCycle( node , edges , visited , currentInStack ):
    visited[node] = True
    currentInStack[node] = True

    neighbours = edges[node]
    for neighbour in neighbours:
        if not visited[neighbour]:
            containsCycle = isNodeInCycle( neighbour , edges , visited , currentInStack )
            if containsCycle:
                return True
        elif currentInStack[neighbour]:
            return True

    currentInStack[node] = False
    return False
        
    
