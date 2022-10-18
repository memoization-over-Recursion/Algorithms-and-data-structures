package twoNumberSum;
import java.util.*;
// O(n) time complexity
// O(n) space complexity
class twoNumberSumOn {
    public static int[] twoNumberSum(int[] array, int targetSum) {
        // array - distinct integer array ( no two ints are the same )
        // targetSum - distinct non negative integer value
        Set<Integer> set = new HashSet<>(); //set allows us to check if a value is in the set in O(1) time as it is based on a hashset
        for (int num : array) {
            if (set.contains(targetSum - num)) {
                return new int[] { num, targetSum - num };
            } else {
                set.add(num);
            }
        }
        return new int[] {};
    }

    public static void main(String args[]) {
        int[] array = new int[] { 2, 1, 3, 4, 5, 6, 9 };
        System.out.println(twoNumberSum(array, 15)[0]);
    }
}
