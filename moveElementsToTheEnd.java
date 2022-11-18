import java.util.*;
//time complexity O( n ) 
//space complexity O( 1 )
class moveElementsToTheEnd {
    public static List<Integer> moveElementToEnd(List<Integer> array, int toMove) {
        int L = 0;
        int R = array.size() - 1;
        while (L < R) {
            if (array.get(L) == toMove && array.get(R) != toMove) {
                swap(array, L, R);
                L++;
                R--;
            } else if (array.get(L) == toMove) {
                R--;
            } else {
                L++;
            }
        }
        return array;

    }

    public static void swap(List<Integer> a, int b, int c) {
        Collections.swap(a, b, c);
    }
}
