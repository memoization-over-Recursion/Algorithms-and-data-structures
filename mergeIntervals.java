import java.util.*;
// time complexity O( nlog(n) )
// space complexity O( n )
public class mergeIntervals {

    public int[][] mergeOverlappingIntervals(int[][] intervals) {
        int[][] sortedInt = intervals.clone();
        Arrays.sort(sortedInt, (a, b) -> Integer.compare(a[0], b[0]));
        List<int[]> mergedInt = new ArrayList<>();
        int[] currentInterval = sortedInt[0];
        mergedInt.add(currentInterval);
        for (int[] a : sortedInt) {
            int[] nextInterval = a;

            if (currentInterval[1] >= nextInterval[0]) {
                currentInterval[1] = Math.max(currentInterval[1], nextInterval[1]);

            } else {
                currentInterval = nextInterval;
                mergedInt.add(currentInterval);

            }
        }
        return mergedInt.toArray(new int[mergedInt.size()][]);
    }
}
