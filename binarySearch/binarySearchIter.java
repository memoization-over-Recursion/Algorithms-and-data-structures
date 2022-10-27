package binarySearch;
//time complexity O( log(n) )
//spacee compleexitty O( 1 )
public class binarySearchIter {
    public static int binarySearch(int[] array, int target) {
        return binSearch(array, target, 0, array.length - 1);
    }

    public static int binSearch(int[] array, int target, int L, int R) {

        while (L <= R) {
            int M = (R + L) / 2;

            if (array[M] == target) {
                return M;
            } else if (array[M] > target) {
                R = M - 1;
            } else {
                L = M + 1;
            }
        }
        return -1;
    }
}
