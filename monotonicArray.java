
// time complexity O( n )
// space complexity O( 1 )
public class monotonicArray {
    public static boolean isMonotonic(int[] array) {
        if (array.length <= 2)
            return true;
        boolean dec = true;
        boolean inc = true;
        for (int i = 1; i < array.length; i++) {
            if (array[i] < array[i - 1]) {
                dec = false;
            }
            if (array[i] > array[i - 1]) {
                inc = false;
            }
        }
        return inc || dec;
    }
}
