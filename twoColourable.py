# time complexity O( v + e )
# sapce complexity O( v )
def twoColorable(edges):
    graph = [None for _ in edges]
    graph[0] = True
    stack = [0]

    while len( stack ) > 0:
        node = stack.pop()
        for connection in edges[ node ]:
            if graph[connection] is None:
                graph[connection] = not graph[node]
                stack.append(connection)
            elif graph[ connection ] == graph[ node ]:
                return False
    return True
    
