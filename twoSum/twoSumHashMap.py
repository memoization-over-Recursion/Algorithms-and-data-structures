# time complexity O( n )
# space complexity O( n )
def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        possibleMatch = targetSum - num
        if possibleMatch in nums:
            return [possibleMatch , num ]
        else:
            nums[ num ] = True
    return []