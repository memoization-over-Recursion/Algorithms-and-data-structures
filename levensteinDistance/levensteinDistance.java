package levensteinDistance;
//time complexity O(mn)
//space complexity O(mn)
public class levensteinDistance {
    
    public static int levenshteinDistance(String str1, String str2) {
        int m = str2.length();
        int n = str1.length();
        int[][] table = new int[m + 1][n + 1];
        table[0][0] = 0;
        for (int i = 1; i <= m; i++) {
            table[i][0] += (table[i - 1][0] + 1);
        }
        for (int j = 1; j <= n; j++) {
            table[0][j] += (table[0][j - 1] + 1);
        }
        for (int i = 1; i < m + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                if (str2.charAt(i - 1) == str1.charAt(j - 1)) {
                    table[i][j] = table[i - 1][j - 1];
                } else {
                    table[i][j] = Math.min(table[i][j - 1], Math.min(table[i - 1][j], table[i - 1][j - 1])) + 1;
                }
            }
        }

        return table[m][n];
    }
}
