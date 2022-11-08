import java.util.*;
//time complexity O( n )
//space complexity O( n )
public class maximizeExpression {

    public int maximizeExpressions(int[] array) {
        if (array.length < 4)
            return 0;
        List<Integer> A = new ArrayList<Integer>(Arrays.asList(array[0]));
        List<Integer> AminB = new ArrayList<Integer>(Arrays.asList(Integer.MIN_VALUE));
        List<Integer> AminBplusC = new ArrayList<Integer>(Arrays.asList(Integer.MIN_VALUE, Integer.MIN_VALUE));
        List<Integer> AminBplusCminD = new ArrayList<Integer>(
                Arrays.asList(Integer.MIN_VALUE, Integer.MIN_VALUE, Integer.MIN_VALUE));
        for (int i = 1; i < array.length; i++) {
            int maxA = Math.max(A.get(i - 1), array[i]);
            A.add(maxA);
        }
        for (int i = 1; i < array.length; i++) {
            int maxAminB = Math.max(AminB.get(i - 1), A.get(i - 1) - array[i]);
            AminB.add(maxAminB);
        }
        for (int i = 2; i < array.length; i++) {
            int maxAminBplusC = Math.max(AminBplusC.get(i - 1), AminB.get(i - 1) + array[i]);
            AminBplusC.add(maxAminBplusC);
        }
        for (int i = 3; i < array.length; i++) {
            int maxAminBplusCminD = Math.max(AminBplusCminD.get(i - 1), AminBplusC.get(i - 1) - array[i]);
            AminBplusCminD.add(maxAminBplusCminD);
        }

        return AminBplusCminD.get(AminBplusCminD.size() - 1);
    }
}
