package minWaitingTime;
import java.util.*;
//time complexity O( nlog(n) )
//space complexity O( 1 )
public class minWaitingTimeFor {
   
    public int minimumWaitingTime(int[] queries) {
        Arrays.sort(queries);
        int total = 0;
        int distance = 0;
        int current = 0;
        for (int i = 0; i < queries.length; i++) {
            current = queries[i];
            distance = queries.length - i - 1;
            total += (current * distance);
        }
        return total;
    }
}
