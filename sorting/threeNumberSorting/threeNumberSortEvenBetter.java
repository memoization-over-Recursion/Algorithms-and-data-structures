package sorting.threeNumberSorting;
// time complexity O(n)
// space complexiity O(1)
public class threeNumberSortEvenBetter {
    public int[] threeNumberSort(int[] array, int[] order) {

        int first = 0;
        int second = 0;
        int third = array.length - 1;

        while (second <= third) {
            int value = array[second];
            if (value == order[0]) {
                swap(array, second, first);
                first++;
                second++;
            } else if (value == order[1]) {
                second++;
            } else {
                swap(array, second, third);
                third--;
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
