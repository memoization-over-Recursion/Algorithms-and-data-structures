//time complexity O( n )
//space complexity O( 1 )
public class firstNonRepeatingCharacter {
    public int firstNonRepeatCharacter(String string) {
        int[] alpha = new int[26];
        for (int i = 0; i < string.length(); i++) {
            alpha[string.charAt(i) - 'a']++;

        }
        for (char c : string.toCharArray()) {
            if (alpha[c - 'a'] == 1) {
                return string.indexOf(c);
            }
        }
        return -1;
    }
}
