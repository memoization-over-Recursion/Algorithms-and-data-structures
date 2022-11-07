import java.util.*;
public class tandemBicycle {
    //time complexity O( nlog(n) )
    //space complexity O( 1 )
    public int tandemBicycles(int[] redShirtSpeeds, int[] blueShirtSpeeds, boolean fastest) {
        int max = 0;
        int min = 0;
        Arrays.sort(redShirtSpeeds);
        Arrays.sort(blueShirtSpeeds);
        for (int i = 0; i < redShirtSpeeds.length; i++) {
            if (fastest) {
                max += Math.max(redShirtSpeeds[i], blueShirtSpeeds[blueShirtSpeeds.length - 1 - i]);
            } else {
                min += Math.max(redShirtSpeeds[i], blueShirtSpeeds[i]);
            }
        }
        return fastest ? max : min;
    }
}
