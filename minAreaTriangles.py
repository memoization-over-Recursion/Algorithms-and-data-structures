#time complexity O( n ^ 2 )
#space complxity O( n )
def minimumAreaRectangle(points):
    col = getCols(points)
    
    minim = float("inf")
    
    parralel = {}
    sortedCol = sorted(col.keys())
    
    for x in sortedCol:
        
        y = col[x]
        y.sort()
        print(y)
        for cur , y2 in enumerate(y):
            
            for prev in range(cur):
                
                y1 = y[prev]
                point = str(y1) +":"+str(y2)

                if(point in parralel):
                    currentArea = (x - parralel[point]) * (y2 - y1)
                    minim = min(minim , currentArea)
                    
                parralel[point] = x
                
    return minim if minim != float("inf") else 0


def getCols(points):
    dict = {}
    for point in (points):
        x , y = point
        if(x not in dict):
            dict[x]  = [y]
        else:
            dict[x].append(y)
    return dict