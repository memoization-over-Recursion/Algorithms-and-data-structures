package numberOfWaysToTraverseAGraph;
// time complexity O( n + m )
// space complexity O( 1 )
public class numOfWaysToTraverseGraphPer {

    public int numberOfWaysToTraverseGraph(int width, int height) {
        int R = width - 1;
        int D = height - 1;
        int rAndD = (R + D);
        int factRAndD = factorial(rAndD);
        int factR = factorial(R);
        int factD = factorial(D);

        return factRAndD / (factR * factD);
    }

    public int factorial(int toBeFactorialed) {
        int result = 1;
        while (toBeFactorialed > 0) {
            result *= (toBeFactorialed);
            toBeFactorialed--;
        }
        return result;
    }
}
