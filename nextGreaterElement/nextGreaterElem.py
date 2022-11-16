#time complexity O( n^2 )
#space complexity O( 1 )
def nextGreaterElement(array):
    ans = [-1] * len(array)
    for i in range(len(array)):
        for j in range(i , len(array)+i):
            if(array[i] < array[j%len(array)]):
                ans[i] = array[j%len(array)]
                break
            else:
                continue
    return ans
    
               