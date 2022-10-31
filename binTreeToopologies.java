//time complexity O(n^2)
//space complexity O(n)
public class binTreeToopologies {
    public static int[] memo = new int[10000];

    public static int numberOfBinaryTreeTopologies(int n) {
        if (n == 0)
            return 1;
        if (memo[n] == 0)
            return memo[n];
        for (int l = 0; l < n; l++) {
            memo[n] += (numberOfBinaryTreeTopologies(l) * numberOfBinaryTreeTopologies(n - 1 - l));
        }
        return memo[n];
    }

}
