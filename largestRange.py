#time complexity O( n )
#space complexity O( n )
def largestRange(array):
    nums = {}
    range = []
    greatest = 0
    for num in array:
        nums[num] = True
    for num in array:
        if( not nums[num]):
            continue
        nums[num] = False 
        current = 1
        left = num - 1
        right = num + 1
        while(left in nums):
            nums[left] = False
            current += 1
            left -= 1
        while(right in nums):
            nums[right] = False
            current += 1
            right += 1
        if(current > greatest):
            greatest = current
            range = [ left + 1 , right - 1 ]
    return range
    
            
        
