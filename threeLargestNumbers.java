//time complexity O( n )
//space complexity O( 1 )
class Program {
    public static int[] findThreeLargestNumbers(int[] array) {
        int[] finalAr = { Integer.MIN_VALUE, Integer.MIN_VALUE, Integer.MIN_VALUE };
        for (int i = 0; i < array.length; i++) {
            if (array[i] > finalAr[2]) {
                update(finalAr, array[i], 2);
            } else if (array[i] > finalAr[1]) {
                update(finalAr, array[i], 1);
            } else if (array[i] > finalAr[0]) {
                update(finalAr, array[i], 0);
            }

        }
        return finalAr;
    }
    public static void update(int[] a, int b, int c) {
        for (int i = 0; i <= c; i++) {
            if (c == i) {
                a[c] = b;
            } else {
                a[i] = a[i + 1];
            }
        }
    }
}
