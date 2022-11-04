package palindromeChecker;
//time complexity O( n )
//space complexity O( 1 )
public class isPalFast {
    public static boolean isPalindrome(String str){
        int start = 0;
        int end = str.length()-1;
        while(start < end){
            if(str.charAt(start) != str.charAt(end)){
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
}
