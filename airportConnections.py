# time complexity O( a * ( a+r ) + a+ r + alog(a) )
# space complexity O( a + r )
def airportConnections(airports, routes, startingAirport):
    graph = makeGraph( airports , routes )
    unreachable = getUnreachable( graph , airports , startingAirport )
    markUnreachableConnections( graph , unreachable )
    return getMin(graph , unreachable )


def getMin(  graph , unreachable  ):
    unreachable.sort(key = lambda a : len(a.unreachableConnections) , reverse = True )
    answer = 0
    for air in unreachable:
        if air.isReachable:
            continue
        answer += 1
        for con in air.unreachableConnections:
            
            graph[con].isReachable = True
    return answer


def makeGraph( ap , routes ):
    graph = {}
    for airport in ap:
        graph[airport] = Node(airport)
    for route in routes:
        airport , connection = route
        graph[airport].connections.append(connection)
    return graph


def getUnreachable( graph , airports , startingAirport ):
    visited = {}
    depthFirstTraverse( graph , startingAirport , visited )
    unreachable = []
    for air in airports:
        if air in visited:
            continue
        node = graph[air]
        node.isReachable = False
        unreachable.append(node)
    return unreachable

def depthFirstTraverse( graph , starting , visited ):
    if starting in visited:
        return 
    visited[starting] = True
    connections = graph[starting].connections
    for connection in connections:
        depthFirstTraverse( graph , connection , visited )

def markUnreachableConnections( graph , unreachable ):
    for node in unreachable:
        port = node.a
        con = []
        depthFirst( graph , port , con , {})
        node.unreachableConnections = con
    

def depthFirst(g , port , u , v ):
    if g[port].isReachable:
        return
    if port in v:
        return
    v[port] = True
    u.append(port)
    con = g[port].connections
    for c in con:
        depthFirst(g , c , u , v )
        
    
class Node:
    def __init__(self , a):
        self.a = a
        self.connections = []
        self.isReachable = True
        self.unreachableConnections = []