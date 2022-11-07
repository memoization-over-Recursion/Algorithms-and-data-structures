package longestCommenSubSequence;
import java.util.*;

// time complexity O( mn )
// space complexity O( mn )
public class longestCommenSubSequenceSimplefast {
    public static List<Character> longestCommonSubsequence(String str1, String str2) {
        int[][] len = new int[str2.length() + 1][str1.length() + 1];
        for (int i = 1; i < str2.length() + 1; i++) {
            for (int j = 1; j < str1.length() + 1; j++) {
                if (str2.charAt(i - 1) == str1.charAt(j - 1)) {
                    len[i][j] = len[i - 1][j - 1] + 1;
                } else {
                    len[i][j] = Math.max(len[i - 1][j], len[i][j - 1]);
                }
            }
        }
        return build(len, str1);
    }
    /* "" X K Y K Z P W
    "" 1  0 0 0 0 0 0 0
    Z  0  0 0 0 0 1 1 1
    X  0  1 1 1 1 1 1 1
    V  0  1 1 1 1 1 1 1
    V  0  1 1 1 1 1 1 1
    Y  0  1 1 2 2 2 2 2
    Z  0  1 1 2 2 3 3 3
    W  0  1 1 2 2 3 3 4 */
    // "str1": "ZXVVYZW",
    // "str2": "XKYKZPW"        
    public static List<Character> build(int[][] len, String s) {
        List<Character> seq = new ArrayList<Character>();
        int i = len.length - 1;
        int j = len[0].length - 1;
        while (i != 0 && j != 0) {
            if (len[i][j] == len[i - 1][j]) {
                i--;
            } else if (len[i][j] == len[i][j - 1]) {
                j--;
            } else {
                seq.add(0, s.charAt(j - 1));
                i--;
                j--;
            }
        }
        return seq;
    }
}