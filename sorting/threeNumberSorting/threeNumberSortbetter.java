package sorting.threeNumberSorting;
//time complexity O(n)
//space complexity O(1)
public class threeNumberSortbetter {
    public int[] threeNumberSort(int[] array, int[] order) {
        int firstElement = order[0];
        int lastElement = order[2];

        int firstIdx = 0;
        for (int i = 0; i < array.length; i++) {
            if (array[i] == firstElement) {
                swap(array, i, firstIdx);
                firstIdx += 1;
            }
        }

        int lastIdx = array.length - 1;
        for (int j = array.length - 1; j >= 0; j--) {
            if (array[j] == lastElement) {
                swap(array, j, lastIdx);
                lastIdx -= 1;
            }
        }
        return array;
    }

    public static void swap(int[] ar, int a, int b) {
        int temp = ar[a];
        ar[a] = ar[b];
        ar[b] = temp;
    }
}
