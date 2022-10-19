import java.util.*;

//time complexity O(n^2)
//space complexity O(n)
public class threeNumberSum {

    public static List<Integer[]> threeNumSum(int[] ar, int tar) {
        Arrays.sort(ar);
        List<Integer[]> answer = new ArrayList<>();
        for (int i = 0; i < ar.length; i++) {
            int num = ar[i];
            int j = i + 1;
            int k = ar.length - 1;
            while (j < k) {
                int num1 = ar[j];
                int num2 = ar[k];
                int sum = num + num1 + num2;
                if (sum == tar) {
                    answer.add(new Integer[] { num, num1, num2 });
                    j++;
                    k--;
                } else if (sum > tar) {
                    k--;
                } else {
                    j++;
                }
            }
        }
        return answer;
    }
}
