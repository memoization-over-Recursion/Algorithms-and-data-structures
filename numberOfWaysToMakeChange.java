public class numberOfWaysToMakeChange {
// time complexity O( nd )
// space complexity O( n )
    public static int numberOfWaysToMakeChan(int n, int[] denoms) {
        int[] amountOfWays = new int[n + 1];
        amountOfWays[0] = 1;
        for (int denom : denoms) {
            for (int amount = 1; amount < (n + 1); amount++) {
                if (denom <= amount) {
                    amountOfWays[amount] += amountOfWays[amount - denom];
                }
            }
        }
        return amountOfWays[n];
    }
}
