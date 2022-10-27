package sorting.mergeSort;

public class mergeSortSpace {
// Best time complexity O(nlog(n))
// Best space complexity O(n)
// Average time complexity O(nlog(n))
// Average space complexity O(n)
// Worst time complexity O(nlog(n))
// Worst space complexity O(n)
    public static int[] mergeSort(int[] array) {
        if (array.length == 1) {
            return array;
        }

        int[] aArray = array.clone();
        mergeSort(array, 0, array.length - 1, aArray);
        return array;
    }

    public static void mergeSort(int[] a, int s, int e, int[] b) {
        if (s == e)
            return;

        int middle = (s + e) / 2;
        mergeSort(b, s, middle, a);
        mergeSort(b, middle + 1, e, a);
        doMerge(a, s, middle, e, b);

    }

    public static void doMerge(int[] a, int s, int m, int e, int[] b) {
        int i = s;
        int j = m + 1;
        int k = s;
        while (i <= m && j <= e) {

            if (b[i] <= b[j]) {
                a[k++] = b[i++];
            } else {
                a[k++] = b[j++];
            }
        }
        while (i <= m) {
            a[k++] = b[i++];
        }
        while (j <= e) {
            a[k++] = b[j++];
        }
    }
}
