package minWaitingTime;
import java.util.*;
// time complexity O( nlog(n) )
//space complexity O( 1 )
public class minimumWaitingTimeWhile {
  public int minimumWaitingTime(int[] queries) {
    Arrays.sort(queries);
    int total = 0;
    int running = 0;
    for(int i = 0; i < queries.length; i++){
      total += running;
      running += queries[i];
    }
    return total;
  }
}
