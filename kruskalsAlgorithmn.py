# time complexity O( e * log( e ) )
# space complexity O( e + v )
def kruskalsAlgorithm(edges):
    edgeList = []
    for i , vertex in enumerate(edges):
        for edge in vertex:
            if edge[0] > i:
                edgeList.append([ i , edge[0] , edge[1] ])
    sortedEdges = sorted(edgeList , key = lambda e : e[2] )
    parents = [v for v in range(len(edges))]
    rnk = [0 for _ in range(len(edges))]
    spanningTree = [[] for _ in range(len(edges))]
    for edge in sortedEdges:
        root1 = find(parents , edge[0])
        root2 = find(parents , edge[1])
        if root1 != root2:
            spanningTree[edge[0]].append([ edge[1] , edge[2] ])
            spanningTree[edge[1]].append([ edge[0] , edge[2] ])

        union(root1 , root2 , parents , rnk)

    return spanningTree
    

# time complexity O( 1 ) 
    # space complexity O( 1 )
def find(parents , value):
    if value != parents[value]:
        parents[value] = find(parents , parents[value])
    return parents[value] 
    
    # time complexity O( 1 ) 
    # space complexity O( 1 )
def union(valueOne, valueTwo , parents , ranks):
    if valueOne not in parents or valueTwo not in parents:
        return

    rootOne = find(parents , valueOne)
    rootTwo = find(parents , valueTwo)
    if ranks[rootOne] < ranks[rootTwo]:
        parents[rootOne] = rootTwo
    elif ranks[rootOne] > ranks[rootTwo]:
        parents[rootTwo] = rootOne
    else:
        parents[rootTwo] = rootOne
        ranks[rootOne] += 1
