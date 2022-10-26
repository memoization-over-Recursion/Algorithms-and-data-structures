package nthFibonnaci;

public class nthFibonnaciMemo {
    //time complexity O(n)
    //space complexity O(n)
    public static  int[] memo = new int[100000];
    public static int nthFibonnaci(int n){
        if(memo[n] != -1){
            return memo[n];
        }

        if( n == 1 )return 0;
        if( n == 2 ) return 1;

        memo[n] = nthFibonnaci(n-1) + nthFibonnaci(n-2);
        return memo[n];
    }
    
}
