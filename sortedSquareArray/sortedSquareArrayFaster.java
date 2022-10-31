package sortedSquareArray;
//time complexity O(n)
//space complexity O(n)
public class sortedSquareArrayFaster {
    public int[] sortedSquaredArray(int[] array) {
        int[] ar = new int[array.length];
        int start = 0; // smallest and largest value
        int end = array.length - 1;
        for (int i = array.length - 1; i >= 0; i--) {
            if (Math.abs(array[end]) > Math.abs(array[start])) {
                ar[i] = array[end] * array[end];
                end--;
            } else {
                ar[i] = array[start] * array[start];
                start++;
            }
        }
        return ar;
    }
}
