#time complexity O( n )
#space complexity O( n )
def sunsetViews(buildings, direction):
    can = []
    start = 0 if direction == 'EAST' else len( buildings ) - 1
    step = 1 if direction == 'EAST' else  -1

    id = start
    while id >= 0 and id < len(buildings):
        bHeight = buildings[id]

        while( len(can) > 0 and buildings[can[-1]] <= bHeight):
            can.pop()
        can.append(id)

        id += step

    if direction == 'WEST':
        return can[::-1]

    return can
        
