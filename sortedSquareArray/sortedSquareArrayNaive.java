package sortedSquareArray;
import java.util.*;
//time complexity O( nlog(n) )
//space complexity O( n )
public class sortedSquareArrayNaive {
    // misleading input -2^2 == 2^2
    public int[] sortedSquaredArray(int[] array) {
        int[] ar = new int[array.length];
        for (int i = 0; i < array.length; i++) {
            ar[i] = array[i] * array[i];
        }
        Arrays.sort(ar);
        return ar;
    }
}
