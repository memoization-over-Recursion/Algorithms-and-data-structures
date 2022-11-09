package maxProfits;
//time complexity O( nk )
//space complexity O( nk )
class maxProfitsWithK {
    public static int maxProfitWithKTransactions(int[] prices, int k) {
        if (prices.length == 0)
            return 0;
        int[][] transactions = new int[k + 1][prices.length];
        for (int i = 0; i < prices.length; i++) {
            transactions[1][i] = 0;
        }
        for (int i = 0; i < k + 1; i++) {
            transactions[i][0] = 0;
        }

        for (int i = 1; i < k + 1; i++) {
            int max = Integer.MIN_VALUE;
            for (int j = 1; j < prices.length; j++) {
                max = Math.max(max, transactions[i - 1][j - 1] - prices[j - 1]);
                transactions[i][j] = Math.max(transactions[i][j - 1], max + prices[j]);
            }
        }
        return transactions[k][prices.length - 1];
    }
}
