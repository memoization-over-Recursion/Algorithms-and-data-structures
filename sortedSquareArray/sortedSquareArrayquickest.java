package sortedSquareArray;
//time complexity O(n)
//space complexity O(n)
public class sortedSquareArrayquickest {
    public int[] sortedSquaredArray(int[] array) {
        int[] finalArray = new int[array.length];
        int start = 0;
        int end = array.length - 1;
        for (int i = array.length - 1; i >= 0; i--) {
            if (Math.abs(array[start]) > Math.abs(array[end])) {
                finalArray[i] = array[start] * array[start];
                start++;
            }
            if (Math.abs(array[start]) < Math.abs(array[end])) {
                finalArray[i] = array[end] * array[end];
                end--;
            }
        }
        return finalArray;
    }
}
