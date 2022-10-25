package sorting;

// Worst time complexity O(n^2) | space complexity O(log(n))
// Best time coomplexity O(nlog(n)) | space coomplexity O(log(n))
// Avg time complexity O(nlog(n)) | space complexity O(log(n))
class quickSort {
    public static int[] quickSortAr(int[] array) {
        quickSortAr(array, 0, array.length - 1);
        return array;
    }

    public static void quickSortAr(int[] ar, int start, int end) {
        if (start >= end)
            return;
        int pivot = start;
        int L = start + 1;
        int R = end;
        while (L <= R) {
            if (ar[L] > ar[pivot] && ar[R] < ar[pivot]) {
                swap(ar, L, R);
            }
            if (ar[L] <= ar[pivot]) {
                L++;
            }
            if (ar[R] >= ar[pivot]) {
                R--;
            }
        }
        swap(ar, pivot, R);
        boolean isSmallestSubarray = R - 1 - start < end - (R + 1);
        if (isSmallestSubarray) {
            quickSortAr(ar, start, R - 1);
            quickSortAr(ar, R + 1, end);
        } else {
            quickSortAr(ar, R + 1, end);
            quickSortAr(ar, start, R - 1);
        }
    }

    public static void swap(int[] ar, int a, int b) {
        int temp = ar[a];
        ar[a] = ar[b];
        ar[b] = temp;
    }
}
