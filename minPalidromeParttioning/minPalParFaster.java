package minPalidromeParttioning;
//time complexity O( n^2 )
//space complexity O( n^2 )
class minPalParFaster {
    public static int palindromePartitioningMinCuts(String str) {
        boolean[][] pal = new boolean[str.length()][str.length()];
        for (int i = 0; i < str.length(); i++) {
            pal[i][i] = true;
        }
        for (int i = 2; i < str.length() + 1; i++) {
            for (int j = 0; j < str.length() - i + 1; j++) {
                int k = i + j - 1;
                if (i == 2) {
                    pal[j][k] = (str.charAt(j) == str.charAt(k));
                } else {
                    pal[j][k] = (str.charAt(j) == str.charAt(k)) && pal[j + 1][k - 1];
                }
            }
        }
        int[] minCuts = new int[str.length()];
        for (int i = 1; i < minCuts.length; i++) {
            minCuts[i] = Integer.MAX_VALUE;
            if (pal[0][i])
                minCuts[i] = 0;
            else {
                minCuts[i] = minCuts[i - 1] + 1;
                for (int j = 1; j < i; j++) {
                    if (pal[j][i] && minCuts[j - 1] + 1 < minCuts[i]) {
                        minCuts[i] = minCuts[j - 1] + 1;
                    }
                }
            }
        }
        return minCuts[minCuts.length - 1];
    }
}
