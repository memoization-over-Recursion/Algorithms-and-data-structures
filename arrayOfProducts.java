import java.util.*;

// time complexity O( n^2 )
// space complexity O( n )
public class arrayOfProducts {
    public int[] arrayOfProduct(int[] array) {
        int[] ar = new int[array.length];
        Arrays.fill(ar, 1);

        for (int i = 0; i < array.length; i++) {
            int L = 0;
            while (L < array.length) {
                if (L == i) {
                    L++;
                } else {
                    ar[i] *= array[L];
                    L++;
                }
            }
        }
        return ar;
    }
}
