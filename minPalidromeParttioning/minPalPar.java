package minPalidromeParttioning;
// time complexity O( n^3 )
// space complexity O( n^2 )
class minPalPar {
    public static int palindromePartitioningMinCuts(String str) {
        boolean[][] pal = new boolean[str.length()][str.length()];
        for (int i = 0; i < str.length(); i++) {
            for (int j = i; j < str.length(); j++) {
                pal[i][j] = isPal(str.substring(i, j + 1));
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

    public static boolean isPal(String toCheck) {
        int start = 0;
        int end = toCheck.length() - 1;
        while (start < end) {
            if (toCheck.charAt(start) != toCheck.charAt(end))
                return false;
            start++;
            end--;
        }
        return true;
    }
}
