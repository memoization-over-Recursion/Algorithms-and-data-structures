//time complexity O( w * h )
//space complexity O( w * h )
public class maximumSumSub {

    public int maximumSumSubmatrix(int[][] matrix, int size) {
        int[][] sums = new int[matrix.length][matrix[0].length];
        int sumUp = 0;
        for (int i = 0; i < matrix.length; i++) {
            sumUp += matrix[i][0];
            sums[i][0] += sumUp;
        }
        int sumUp2 = 0;
        for (int i = 0; i < matrix[0].length; i++) {
            sumUp2 += matrix[0][i];
            sums[0][i] += sumUp2;
        }
        sums[0][0] -= matrix[0][0];
        for (int i = 1; i < matrix.length; i++) {
            for (int j = 1; j < matrix[i].length; j++) {
                sums[i][j] += (sums[i - 1][j] + sums[i][j - 1]);
                sums[i][j] -= sums[i - 1][j - 1];
                sums[i][j] += matrix[i][j];
            }
        }
        int maxSum = Integer.MIN_VALUE;
        for (int k = size - 1; k < sums.length; k++) {
            for (int l = size - 1; l < sums[k].length; l++) {
                int total = sums[k][l];
                boolean touchesTop = (k - size < 0);
                if (!touchesTop) {
                    total -= sums[k - size][l];
                }

                boolean touchesLeft = (l - size < 0);
                if (!touchesLeft) {
                    total -= sums[k][l - size];
                }

                boolean touchesEither = (touchesTop || touchesLeft);
                if (!touchesEither) {
                    total += sums[k - size][l - size];
                }
                maxSum = Math.max(maxSum, total);
            }
        }
        return maxSum;
    }
}
