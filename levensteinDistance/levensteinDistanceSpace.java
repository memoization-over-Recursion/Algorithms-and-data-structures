package levensteinDistance;

// time complexity O(mn)
// space complexity O(min(m , n))
public class levensteinDistanceSpace {
    
    public static int levenshteinDistance(String str1, String str2) {
        String small = str1.length() >= str2.length() ? str2 : str1;
        String big = str1.length() >= str2.length() ? str1 : str2;
        int[] evenEdits = new int[small.length() + 1];
        int[] oddEdits = new int[small.length() + 1];
        for (int j = 0; j < small.length() + 1; j++) {
            evenEdits[j] = j;
        }
        int[] current;
        int[] previous;
        for (int i = 1; i < big.length() + 1; i++) {
            if (i % 2 == 1) {
                current = oddEdits;
                previous = evenEdits;
            } else {
                current = evenEdits;
                previous = oddEdits;
            }
            current[0] = i;
            for (int j = 1; j < small.length() + 1; j++) {
                if (big.charAt(i - 1) == small.charAt(j - 1)) {
                    current[j] = previous[j - 1];
                } else {
                    current[j] = 1 + Math.min(previous[j - 1], Math.min(previous[j], current[j - 1]));
                }
            }

        }
        return big.length() % 2 == 0 ? evenEdits[small.length()] : oddEdits[small.length()];
    }
}
