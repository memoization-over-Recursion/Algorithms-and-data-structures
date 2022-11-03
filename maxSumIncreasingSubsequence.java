import java.util.*;
// time complexity O(n^2)
// space complexity O(n)
class maxSumIncreasingSubsequence {
    public static List<List<Integer>> maxSumIncreasingSubsequences(int[] array) {
        int[] sums = array.clone();
        int currentSumIdx = 0;
        int[] sequence = new int[array.length];
        Arrays.fill(sequence, Integer.MIN_VALUE);
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < i; j++) {
                if (array[j] < array[i] && sums[j] + array[i] >= sums[i]) {
                    sums[i] = sums[j] + array[i];
                    sequence[i] = j;
                }
            }
            if (sums[i] >= sums[currentSumIdx]) {
                currentSumIdx = i;
            }
        }
        return buildSequence(array, sequence, currentSumIdx, sums[currentSumIdx]);
    }

    public static List<List<Integer>> buildSequence(int[] a, int[] s, int cur, int sums) {
        List<List<Integer>> sequence = new ArrayList<List<Integer>>();
        sequence.add(new ArrayList<Integer>());
        sequence.add(new ArrayList<Integer>());
        sequence.get(0).add(sums);
        while (cur != Integer.MIN_VALUE) {
            sequence.get(1).add(0, a[cur]);
            cur = s[cur];
        }
        return sequence;
    }
}
