package powerSet;
import java.util.*;
// O(n*2^n) time complexity
// O(n*2^n) space complexity
public class powerSetRecOn2n {
    public static List<List<Integer>> powerset(List<Integer> array) {
        return powerset(array, array.size() - 1);
    }

    public static List<List<Integer>> powerset(List<Integer> array, int idx) {
        if (idx < 0) {
            List<List<Integer>> emptySet = new ArrayList<List<Integer>>();
            emptySet.add(new ArrayList<Integer>());
            return emptySet;
        }
        int element = array.get(idx);
        List<List<Integer>> subsets = powerset(array, idx - 1);
        int len = subsets.size();
        for (int i = 0; i < len; i++) {
            List<Integer> current = new ArrayList<Integer>(subsets.get(i));
            current.add(element);
            subsets.add(current);
        }
        return subsets;
    }
}
