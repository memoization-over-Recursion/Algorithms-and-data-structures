package palindromeChecker;
//time complexity O( n^2 )
//space complexity O( n )
public class isPalSlow {
    public static boolean isPalindrome(String str) {
        String reverse = "";
        for(int i = str.length()-1 ; i >= 0 ; i--){
            reverse += str.charAt(i);
        }
        return str.equals(reverse);
    }
}
