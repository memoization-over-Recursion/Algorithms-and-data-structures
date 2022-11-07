import java.util.*;
//time complexity O( n )
//space  complexity O( n )
public class branchSums {
    
    public static class BinaryTree {
        int value;
        BinaryTree left;
        BinaryTree right;

        BinaryTree(int value) {
            this.value = value;
            this.left = null;
            this.right = null;
        }
    }

    public static List<Integer> branchSum(BinaryTree root) {
        List<Integer> ar = new ArrayList<Integer>();
        helper(root, 0, ar);
        return ar;
    }

    public static void helper(BinaryTree root, int runningSum, List<Integer> ar) {
        if (root == null)
            return;
        int newSum = runningSum + root.value;
        if (root.left == null && root.right == null) {
            ar.add(newSum);
        }
        helper(root.left, newSum, ar);
        helper(root.right, newSum, ar);
    }
}
