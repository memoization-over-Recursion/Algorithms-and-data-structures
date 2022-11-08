package maxProfits;
//time cmplexity O( nk )
//space complexity O( n )
public class maxProfitsWithKSmaller {

    public static int maxProfitWithKTransactions(int[] prices, int k) {
        if (prices.length == 0)
            return 0;
        int[] even = new int[prices.length];
        int[] odd = new int[prices.length];

        int[] current;
        int[] previous;
        for (int i = 1; i < k + 1; i++) {
            if (i % 2 == 0) {
                current = even;
                previous = odd;
            } else {
                current = odd;
                previous = even;
            }
            int max = Integer.MIN_VALUE;
            for (int j = 1; j < prices.length; j++) {
                max = Math.max(max, previous[j - 1] - prices[j - 1]);
                current[j] = Math.max(current[j - 1], max + prices[j]);
            }
        }
        return k % 2 == 0 ? even[prices.length - 1] : odd[prices.length - 1];
    }
}
