package firstDuplicateValue;
import java.util.*;

// time complexity O( n )
// space complexity O( n )
public class firstDuplicateValueHash {

    public int firstDuplicateValue(int[] array) {
        HashSet<Integer> map = new HashSet<Integer>();
        for (int i : array) {
            if (map.contains(i)) {
                return i;
            }
            map.add(i);
        }
        return -1;
    }
}
