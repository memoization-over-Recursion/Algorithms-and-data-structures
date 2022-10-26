package nthFibonnaci;
public class nthFibonnaciRec {
    //time complexity O(2^n)
    //space complexity O(n)
    public static int nthFibonnaci(int n){
        if(n == 1)return 0;
        if(n == 2)return 1;

        return nthFibonnaci(n-1)+nthFibonnaci(n-2); 
    }
}
