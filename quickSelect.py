#best time complexity O( n )
#best space complexity O ( 1 )
#worst time complexity O( n^2 )
#worst space complexity O ( 1 )
def quickselect(array, k):
    pos = k-1
    return helper(array , 0 , len(array) - 1 , pos)

def helper(ar , s , e , pos):
    while True:
        if(s > e):
            raise Exception("algo fucky")
        p = s
        L = s+1
        R = e
        while( L <= R ):
            if(ar[L] > ar[p] and ar[R] < ar[p]):
                swap( ar , L , R )
            if(ar[L] <= ar[p]):
                L += 1
            if(ar[R] >= ar[p]):
                R -= 1
        swap(ar , p , R)
        if(R == pos):
            return ar[R]
        elif(R < pos):
            s  = R + 1
        else:
            e = R - 1



def swap(arr , i , j ):
    arr[i] , arr[j] = arr[j] , arr[i]