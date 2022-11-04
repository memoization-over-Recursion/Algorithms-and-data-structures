package palindromeChecker;
//time complexity O( n )
//space complexity O( n )
public class isPalRec {
    public static boolean isPalindrome(String str){
        return isPalindrome(str , 0);
    }

    public static boolean isPalindrome(String str , int a){
        int j = str.length()-1-a;
        return a >= j ? true : str.charAt(a) == str.charAt(j) && isPalindrome(str , a+1);
    }
}
