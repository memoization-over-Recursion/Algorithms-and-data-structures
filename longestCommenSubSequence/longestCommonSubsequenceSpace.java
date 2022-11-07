package longestCommenSubSequence;
import java.util.*;

// time complexity O(mn * min( m , n ))
// space complexity O( min( m , n )^2 )
public class longestCommonSubsequenceSpace {
    public static List<Character> longestCommonSubsequence(String str1, String str2) {
        String small = str1.length() < str2.length() ? str1 : str2;
        String big = str1.length() >= str2.length() ? str1 : str2;
        List<List<Character>> even = new ArrayList<List<Character>>();
        List<List<Character>> odd = new ArrayList<List<Character>>();
        for (int i = 0; i < small.length() + 1; i++) {
            even.add(new ArrayList<Character>());
            odd.add(new ArrayList<Character>());
        }
        for (int j = 1; j < big.length() + 1; j++) {
            List<List<Character>> current;
            List<List<Character>> previous;

            if (j % 2 == 1) {
                current = odd;
                previous = even;
            } else {
                current = even;
                previous = odd;
            }
            for (int k = 1; k < small.length() + 1; k++) {
                if (big.charAt(j - 1) == small.charAt(k - 1)) {
                    List<Character> c = new ArrayList<Character>(previous.get(k - 1));
                    current.set(k, c);
                    current.get(k).add(big.charAt(j - 1));
                } else {
                    if (previous.get(k).size() > current.get(k - 1).size()) {
                        current.set(k, previous.get(k));
                    } else {
                        current.set(k, current.get(k - 1));
                    }
                }
            }
        }
        return big.length() % 2 == 0 ? even.get(small.length()) : odd.get(small.length());
    }
}
