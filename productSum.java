   import java.util.*;

public class productSum{
    //time complexity O( n )
    //space complexity O( d )
    public static int productSums(List<Object> array) {
        return productSumHelper(array, 1);
    }

    public static int productSumHelper(List<Object> array, int a) {
        int sum = 0;
        for (Object o : array) {
            if (o instanceof List) {
                @SuppressWarnings("unchecked")
                List<Object> our = (List<Object>) o;
                sum += productSumHelper(our, a + 1);
            } else {
                sum += (int) o;
            }

        }
        return sum * a;
    }

}
