package waterArea;
// time complexity O( n )
// space complexitY O( 1 )
public class waterAreaBetterSpace{
    public static int waterArea(int[] heights) {
        if (heights.length == 0)
            return 0;

        int left = 0;
        int right = heights.length - 1;
        int leftMax = heights[left];
        int rightMax = heights[right];
        int surfaceArea = 0;

        while (left < right) {
            if (heights[left] < heights[right]) {
                left++;
                leftMax = Math.max(leftMax, heights[left]);
                surfaceArea += leftMax - heights[left];
            } else {
                right--;
                rightMax = Math.max(rightMax, heights[right]);
                surfaceArea += rightMax - heights[right];
            }
        }
        return surfaceArea;
    }
}
