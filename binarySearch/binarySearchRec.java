package binarySearch;
//time complexity O( log(n) )
//space complexity O( log(n) )
public class binarySearchRec {
    public static int binarySearch(int[] array, int target) {
        return binSearch(array, target, 0, array.length - 1);
    }

    public static int binSearch(int[] array, int target, int L, int R) {

        if (L <= R) {
            int M = L + (R - L) / 2;

            if (array[M] == target) {
                return M;
            }
            if (array[M] > target) {
                return binSearch(array, target, L, M - 1);
            }
            return binSearch(array, target, M + 1, R);
        }
        return -1;
    }
    
}
