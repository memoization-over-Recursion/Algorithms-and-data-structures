package palindromeChecker;
//time complexity O( n )
//space complexity O( n )
public class isPalStringBuilder {
    public static boolean isPalindrome(String str) {
        StringBuilder reverse = new StringBuilder();
        for (int i = str.length() - 1; i >= 0; i--) {
            reverse.append(str.charAt(i));
        }
        return str.equals(reverse.toString());
    }
}
