import java.util.*;
//time complexity O( n )
//space complexity O( n )
public class balancedBrackets {
    public static boolean balancedBracket(String str) {
        
        Stack<Character> openingBrackets = new Stack<Character>();
        for (Character c : str.toCharArray()) {
            if (c == ']' && !openingBrackets.isEmpty() && openingBrackets.peek() == '[') {
                openingBrackets.pop();
            } else if (c == ')' && !openingBrackets.isEmpty() && openingBrackets.peek() == '(') {
                openingBrackets.pop();
            } else if (c == '}' && !openingBrackets.isEmpty() && openingBrackets.peek() == '{') {
                openingBrackets.pop();
            } else {
                if (c == '{' || c == '}' || c == '[' || c == ']' || c == '(' || c == ')')
                    openingBrackets.push(c);
            }
        }
        return openingBrackets.isEmpty();
    }
}
