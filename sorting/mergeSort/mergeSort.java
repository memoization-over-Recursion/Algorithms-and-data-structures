package sorting.mergeSort;
import java.util.*;

// Best time complexity O(nlog(n))
// Best space complexity O(nlog(n))
// Average time complexity O(nlog(n))
// Average space complexity O(nlog(n))
// Worst time complexity O(nlog(n))
// Worst space complexity O(nlog(n))
class mergeSort {
    public static int[] mergeSortNormal(int[] array) {
        if (array.length == 1) {
            return array;
        }

        int middle = array.length / 2;
        int[] a1 = Arrays.copyOfRange(array, 0, middle);
        int[] a2 = Arrays.copyOfRange(array, middle, array.length);
        return mergeTwoArrays(mergeSortNormal(a1), mergeSortNormal(a2));

    }

    public static int[] mergeTwoArrays(int[] a, int[] b) {
        int[] merged = new int[a.length + b.length];
        int i = 0;
        int j = 0;
        while (i < a.length && j < b.length) {
            int k = i + j;
            if (a[i] <= b[j]) {
                merged[k] = a[i];
                i++;
            } else {
                merged[k] = b[j];
                j++;
            }
        }
        int k = i + j;
        while (i < a.length) {
            merged[k++] = a[i++];
        }
        while (j < b.length) {
            merged[k++] = b[j++];
        }
        return merged;
    }
}
