#time complexity O( n )
#space complexity O( n )
def nextGreaterElement(array):
    ans = [-1] * len(array)
    stack = []
    for id in range( 2 * len(array) ):
        circ = id % len(array)

        while len(stack) > 0 and array[stack[-1]] < array[circ]:
            top = stack.pop()
            ans[top] = array[circ]
        stack.append(circ)
    return ans
