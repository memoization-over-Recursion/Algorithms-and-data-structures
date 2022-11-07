package minNumOfJumps;
// time complexity O( n )
// space complexity O( 1 )
public class minNumOfJumpsFast {
    public static int minNumberOfJumps(int[] array) {
        if (array.length == 1)
            return 0;
        int maxReach = array[0];
        int steps = array[0];
        int jumps = 0;
        for (int i = 1; i < array.length - 1; i++) {
            maxReach = Math.max(maxReach, array[i] + i);
            steps--;
            if (steps == 0) {
                jumps += 1;
                steps = maxReach - i;
            }
        }
        return jumps + 1;
    }
}
