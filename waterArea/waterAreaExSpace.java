package waterArea;
// time complexity O( n )
// space complexity O ( n )
public class waterAreaExSpace {
    public static int waterArea(int[] heights) {
        int[] maxes = new int[heights.length];
        int leftMax = 0;
        for (int i = 0; i < heights.length; i++) {
            maxes[i] = leftMax;
            leftMax = Math.max(leftMax, heights[i]);
        }
        int rightMax = 0;
        for (int j = heights.length - 1; j >= 0; j--) {
            int minHeight = Math.min(rightMax, maxes[j]);
            if (heights[j] < minHeight) {
                maxes[j] = minHeight - heights[j];
            } else {
                maxes[j] = 0;
            }
            rightMax = Math.max(rightMax, heights[j]);
        }

        int total = 0;
        for (int i : maxes) {
            total += i;
        }
        return total;
    }
}
