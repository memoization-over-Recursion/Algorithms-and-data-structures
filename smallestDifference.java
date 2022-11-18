import java.util.*;
// time complexity( nlog(n) + mlog(m) )
// space complexity O( 1 )
public class smallestDifference {
    public static int[] smallestDifferences(int[] arrayOne, int[] arrayTwo) {

        Arrays.sort(arrayOne);
        Arrays.sort(arrayTwo);
        int i = 0;
        int j = 0;
        int smallestDifference = Integer.MAX_VALUE;
        int[] smallest = new int[2];
        while (i < arrayOne.length && j < arrayTwo.length) {
            int currentDifference = Math.abs(arrayOne[i] - arrayTwo[j]);
            if (currentDifference < smallestDifference) {
                smallestDifference = currentDifference;
                smallest[0] = arrayOne[i];
                smallest[1] = arrayTwo[j];
            }

            if (arrayOne[i] == arrayTwo[j]) {
                return new int[] { arrayOne[i], arrayTwo[j] };
            } else if (arrayOne[i] < arrayTwo[j]) {
                i++;
            } else {
                j++;
            }

        }
        return smallest;
    }
}
