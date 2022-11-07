package longestCommenSubSequence;
import java.util.*;
// time complexity O( mn )
// space complexity O( mn )
public class longestCommonSubsequenceFast {
    public static List<Character> longestCommonSubsequence(String str1, String str2) {
        int[][][] lcs = new int[str2.length() + 1][str1.length() + 1][];
        for (int i = 0; i < str2.length() + 1; i++) {
            for (int j = 0; j < str1.length() + 1; j++) {
                lcs[i][j] = new int[] { 0, 0, 0, 0 };
            }
        }
        for (int i = 1; i < str2.length() + 1; i++) {
            for (int j = 1; j < str1.length() + 1; j++) {
                if (str2.charAt(i - 1) == str1.charAt(j - 1)) {
                    int[] newEntry = new int[] { (int) str2.charAt(i - 1), lcs[i - 1][j - 1][1] + 1, i - 1, j - 1 };
                    lcs[i][j] = newEntry;
                } else {
                    if (lcs[i - 1][j][1] > lcs[i][j - 1][1]) {
                        int[] newEntry = new int[] { -1, lcs[i - 1][j][1], i - 1, j };
                        lcs[i][j] = newEntry;
                    } else {
                        int[] newEntry = new int[] { -1, lcs[i][j - 1][1], i, j - 1 };
                        lcs[i][j] = newEntry;
                    }
                }
            }
        }
        return build(lcs);
    }

    public static List<Character> build(int[][][] lcs) {
        List<Character> seq = new ArrayList<Character>();
        int i = lcs.length - 1;
        int j = lcs[0].length - 1;
        while (i != 0 && j != 0) {
            int[] current = lcs[i][j];
            if (current[0] != -1) {
                seq.add(0, (char) current[0]);
            }
            i = current[2];
            j = current[3];
        }
        return seq;
    }
}
