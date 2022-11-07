import java.util.*;

// time complexity O( ij )
// space complexity O( ij )
class knapsackSolutionDynam {
    public static List<List<Integer>> knapsackProblem(int[][] items, int capacity) {
        int[][] values = new int[items.length + 1][capacity + 1];
        for (int i = 1; i < values.length; i++) {
            int w = items[i - 1][1];
            int v = items[i - 1][0];
            for (int j = 1; j < values[i].length; j++) {
                if (w <= j) {
                    values[i][j] = Math.max(values[i - 1][j], values[i - 1][j - w] + v);
                } else {
                    values[i][j] = values[i - 1][j];
                }
            }
        }
        return build(values, items, values[items.length][capacity]);
    }

    public static List<List<Integer>> build(int[][] values, int[][] items, int maxValue) {
        List<List<Integer>> seq = new ArrayList<List<Integer>>();
        List<Integer> totalWeight = new ArrayList<Integer>();
        totalWeight.add(maxValue);
        seq.add(totalWeight);
        seq.add(new ArrayList<Integer>());
        int i = values.length - 1;
        int j = values[0].length - 1;
        while (i > 0) {
            if (values[i][j] == values[i - 1][j]) {
                i--;
            } else {
                seq.get(1).add(0, i - 1);
                j -= items[i - 1][1];
                i--;
            }
            if (j == 0)
                break;
        }
        return seq;
    }
}
