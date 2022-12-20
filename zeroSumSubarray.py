#time complexity O( n ) 
#space complexity O( n )
def zeroSumSubarray(nums):
    sums = set([0])
    current = 0
    for num in nums:
        current += num
        if current in sums:
            return True
        sums.add(current)
    return False

# [ 4 -3 2 4 -1 -5 7 ]
