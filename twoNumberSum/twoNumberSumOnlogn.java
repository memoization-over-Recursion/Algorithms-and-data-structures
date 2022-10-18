package twoNumberSum;
import java.util.*;
// O(nlogn) time complexity
// O(1) space complexity
public class twoNumberSumOnlogn {
    public static int[] twoNumberSum(int[] array, int targetSum) {
    // array - distinct integer array ( no two ints are the same )
    // targetSum - distinct non negative integer value
    Arrays.sort(array);
    int left = 0;
    int right = array.length - 1;
    //binary search esque solution to find the two values within the array that solve our problem
    while (left < right) {
        int current = array[left] + array[right];
        if (current == targetSum) {
            return new int[] { array[left], array[right] };
        }
        if (current < targetSum) {
            left++;
        }
        if (current > targetSum) {
            right--;
        }

    }
    return new int[] {};
    }
}
