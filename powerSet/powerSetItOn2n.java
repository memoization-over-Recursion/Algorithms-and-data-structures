package powerSet;
import java.util.*;
// O(n*2^n) time complexity
// O(n*2^n) space complexity
class Program {
    public static List<List<Integer>> powerset(List<Integer> array) {
        List<List<Integer>> ar = new ArrayList<List<Integer>>();
        ar.add(new ArrayList<Integer>());
        for (Integer ae : array) {
            int size = ar.size();
            for (int j = 0; j < size; j++) {
                List<Integer> a = new ArrayList<Integer>(ar.get(j));
                a.add(ae);
                ar.add(a);
            }
        }
        return ar;
    }
}
