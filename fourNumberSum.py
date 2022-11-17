#time complexity O( n^2 )
#space complexity O( n^2 )
def fourNumberSum(array, targetSum):
    sums = {}
    answer = []
    for i in range( 1 , len(array)-1):
        for j in range( i+1 , len(array)):
            sumer = array[i]+array[j]
            remaining = targetSum - sumer
            if(remaining in sums):
                for sum in sums[remaining]:
                    answer.append(sum + [array[i] , array[j]])
        for k in range(0 , i):
            sum = array[i] + array[k]
            if(sum not in sums):
                sums[sum] = [[array[k] , array[i]]]
            else:
                sums[sum].append([array[k] , array[i]])
            
    return answer
            