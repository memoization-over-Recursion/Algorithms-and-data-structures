#time complexity O( n )
#space complexity O( n ) 
def zigzagTraverse(array):
    height = len(array) - 1
    width = len(array[0]) - 1
    row = 0
    col = 0
    down = True
    result = []
    while not outOfBounds(row , col , height , width ):
        result.append(array[row][col])
        
        if(down):
            if(col == 0 or row == height):
                down = False
                if(row==height):
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if(row == 0 or col == width):
                down = True
                if(col == width):
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1
    return result
            
        
       
                
        

def outOfBounds(row , col , height , width):
    return row < 0 or col < 0 or row > height or col > width

# 1 1 1 1 
# 1 1 1 1
# 1 1 1 1
# 1 1 1 1
