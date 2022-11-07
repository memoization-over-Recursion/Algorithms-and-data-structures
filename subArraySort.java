// time complexity O( n )
// space complexity O( 1 )
public class subArraySort {
    public static int[] subarraySort(int[] array) {
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < array.length; i++) {
            if (isOutOfOrder(array, i)) {
                min = Math.min(min, array[i]);
                max = Math.max(max, array[i]);
            }
        }
        if (min == Integer.MAX_VALUE) {
            return new int[] { -1, -1 };
        }
        int g = 0;
        while (min >= array[g]) {
            g++;
        }
        int h = array.length - 1;
        while (max <= array[h]) {
            h--;
        }
        return new int[] { g, h };
    }

    public static boolean isOutOfOrder(int[] ar, int a) {
        if (a == 0) {
            return ar[a] > ar[a + 1];
        } else if (a == ar.length - 1) {
            return ar[a - 1] > ar[a];
        } else {
            return ar[a - 1] > ar[a] || ar[a] > ar[a + 1];
        }
    }
}
