#time complexity O( v^2 + e )
#space complexity O( v )
def dijkstrasAlgorithm(start, edges):
    #directed positive edges
    #only directed positive edges
    #no self loop
    seenNodes = set()
    min = [float("inf") for _ in range( len( edges ) ) ]
    min[start] = 0
    n = len( edges )

    while( len( seenNodes ) < n ):
        vertex , distance = getMinV( min , seenNodes )
        if(distance == float("inf")):
            break

        seenNodes.add(vertex)
        
        for line in edges[vertex]:
            destin , distance2des = line
            
            if(destin in seenNodes):
                continue
                
            appendedPath = distance + distance2des
            current = min[destin]
            if(appendedPath < current):
                min[destin] = appendedPath
    
    print(min)
    return list(map(lambda x: -1 if x == float('inf') else x , min))




def getMinV(dis,visited):
    minim = float('inf')
    vertex = -1

    for vert, dise in enumerate(dis):
        if(vert in visited):
            continue
        if(dise <= minim):
            vertex = vert
            minim = dise

    return vertex , minim

    
    
    
    
    