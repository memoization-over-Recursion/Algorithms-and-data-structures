// time complexity O( n )
// space complexity O( 1 )
public class longestPeak {
    public static int longestPeaks(int[] array) {
        int longestPeak = 0;
        int i = 1;

        while (i < array.length - 1) {
            boolean isPeak = array[i] > array[i - 1] && array[i] > array[i + 1] ? true : false;
            if (!isPeak) {
                i++;
                continue;
            }
            int L = i - 2;
            while (L >= 0 && array[L] < array[L + 1]) {
                L--;
            }

            int R = i + 2;
            while (R < array.length && array[R] < array[R - 1]) {
                R++;
                System.out.println(array[R - 1]);

            }

            int currentPeak = R - L - 1;
            longestPeak = Math.max(currentPeak, longestPeak);

            i = R;

        }
        return longestPeak;
    }
}
