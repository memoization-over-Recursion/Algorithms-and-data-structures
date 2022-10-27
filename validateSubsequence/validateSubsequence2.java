package validateSubsequence;
import java.util.*;
//time complexity O(n)
//space complexity O(1)
public class validateSubsequence2 {
    public static boolean isValidSubsequence(List<Integer> array, List<Integer> sequence) {
        int left = 0;
        int left1 = 0;
        while (left < array.size() && left1 < sequence.size()) {
            if (array.get(left) == sequence.get(left1)) {
                left1++;
            }
            left++;
        }
        if (left1 == sequence.size())
            return true;
        return false;
    }
}
