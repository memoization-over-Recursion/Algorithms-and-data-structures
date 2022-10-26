package nthFibonnaci;

public class nthFibonnaciO1space {
    public static int nthFibonnaci(int n){
        int[] firstTwo = new int[]{0,1};
        int counter = 1;
        while(counter < n){
            int nxt = firstTwo[0] + firstTwo[1];
            firstTwo[0] = firstTwo[1];
            firstTwo[1] = nxt;
            counter++;
        }
        return firstTwo[0];
    }
    
}
