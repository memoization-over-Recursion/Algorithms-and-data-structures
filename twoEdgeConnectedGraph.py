# time complexity O( v + e )
# space complexity O( v )
def twoEdgeConnectedGraph(edges):
    if len(edges) == 0:
        return True

    arrivals = [-1] * len( edges )
    start = 0

    if getMinArrivalTime( start , -1 , 0 , arrivals , edges) == -1:
        return False

    return areAllVisited(arrivals)
    
def areAllVisited( m ):
    for i in m:
        if i == -1:
            return False
    return True

def getMinArrivalTime( start , a , b , arrivals , edges):
    arrivals[start] = b
    minim = b

    for des in edges[start]:
        if arrivals[des] == -1:
            minim = min( minim ,  getMinArrivalTime( des , start , b+1 , arrivals , edges))
        elif des != a:
            minim = min( minim , arrivals[ des ])

    if minim == b and a != -1:
        return -1


    return minim