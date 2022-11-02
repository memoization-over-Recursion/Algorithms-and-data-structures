package numberOfWaysToTraverseAGraph;
//time complexity O( mn )
//space complexity O( mn )
public class numOfWaysOfTraverseGraphDyn {

    public int numberOfWaysToTraverseGraph(int width, int height) {
        int[][] ways = new int[width + 1][height + 1];
        for (int i = 1; i < ways.length; i++) {
            for (int j = 1; j < ways[i].length; j++) {
                if (i == 1 || j == 1) {
                    ways[i][j] = 1;
                } else {
                    ways[i][j] = ways[i - 1][j] + ways[i][j - 1];
                }
            }
        }
        return ways[ways.length - 1][ways[0].length - 1];
    }
}
