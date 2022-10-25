package sorting.threeNumberSorting;
// time complexity O(n)
// space complexity O(1)
class threeNumberSortingNaive {
    public int[] threeNumberSort(int[] array, int[] order) {
        int[] freq = new int[] { 0, 0, 0 };
        for (int a : array) {
            int in = getIndex(order, a);
            freq[in]++;
        }
        for (int i = 0; i < 3; i++) {
            int count = freq[i];
            int element = order[i];
            int previousSum = sum(freq, i);
            for (int n = 0; n < count; n++) {
                int idx = previousSum + n;
                array[idx] = element;
            }

        }
        return array;
    }

    public static int getIndex(int[] ar, int elem) {
        for (int i = 0; i < ar.length; i++) {
            if (ar[i] == elem) {
                return i;
            }
        }
        return -1;
    }

    public static int sum(int[] arr, int i) {
        int sum = 0;
        for (int h = 0; h < i; h++) {
            sum += arr[h];
        }
        return sum;
    }
}
