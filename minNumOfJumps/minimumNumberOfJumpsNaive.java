package minNumOfJumps;
import java.util.*;
// time complexity O( n^2 )
// space complexity O( n )
public class minimumNumberOfJumpsNaive {
    public static int minNumberOfJumps(int[] array) {
        int[] copy = new int[array.length];
        Arrays.fill(copy, Integer.MAX_VALUE);
        copy[0] = 0;
        for (int i = 1; i < array.length; i++) {
            for (int j = 0; j < i; j++) {
                if (array[j] + j >= i) {
                    copy[i] = Math.min(copy[i], copy[j] + 1);
                }
            }
        }
        return copy[copy.length - 1];

    }
}
