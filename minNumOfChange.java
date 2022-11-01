import java.util.*;
//time complexity O(dn)
//space complexity O(n)
public class minNumOfChange {
    public static int minNumberOfCoinsForChange(int n, int[] denoms) {
        int[] ways = new int[n + 1];
        int c = 0;
        Arrays.fill(ways, Integer.MAX_VALUE);
        ways[0] = 0;
        for (int denom : denoms) {
            for (int i = 1; i < ways.length; i++) {
                if (denom <= i) {
                    c = (ways[i - denom] == Integer.MAX_VALUE) ? ways[i - denom] : ways[i - denom] + 1;
                    ways[i] = Math.min(c, ways[i]);

                }
            }
        }
        return ways[n] != Integer.MAX_VALUE ? ways[n] : -1;
    }
}
