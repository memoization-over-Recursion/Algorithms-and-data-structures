package flattenBinaryTree;
//O(n) time complexity
//O(d) space complexity
public class flattenBinaryTreed {
    // BinaryTree - A tree with left and right data fields
    public static BinaryTree flattenBinaryTree(BinaryTree root) {
        return flattenTree(root)[0];
    }

    //leftMost null
    //rightMost null
    //leftAndRightMostNodes = null , null
    public static BinaryTree[] flattenTree(BinaryTree t1) {
        BinaryTree leftMost;
        BinaryTree rightMost;

        if (t1.left == null) {
            leftMost = t1;
        } else {
            BinaryTree[] leftAndRightMostNodes = flattenTree(t1.left);
            connectNodes(leftAndRightMostNodes[1], t1);
            leftMost = leftAndRightMostNodes[0];
        }

        if (t1.right == null) {
            rightMost = t1;
        } else {
            BinaryTree[] leftAndRightMostNodes = flattenTree(t1.right);
            connectNodes(t1, leftAndRightMostNodes[0]);
            rightMost = leftAndRightMostNodes[1];
        }

        return new BinaryTree[] { leftMost, rightMost };
    }

    public static void connectNodes(BinaryTree left, BinaryTree right) {
        left.right = right;
        right.left = left;
    }

    // This is the class of the input root. Do not edit it.
    static class BinaryTree {
        int value;
        BinaryTree left = null;
        BinaryTree right = null;

        public BinaryTree(int value) {
            this.value = value;
        }
    }
}
