

import java.util.*;

// time complexity O( nlog( n ) )
// space complexity O( 1 )
public class nonConstructibleChange {
    // each value is uniquee and can only be used once
    public int nonConstructChange(int[] coins) {
        Arrays.sort(coins);
        int change = 0;
        for (int i = 0; i < coins.length; i++) {
            if (coins[i] > (change + 1)) {
                return (change + 1);
            }
            change += coins[i];
        }
        return change + 1;
    }
}
