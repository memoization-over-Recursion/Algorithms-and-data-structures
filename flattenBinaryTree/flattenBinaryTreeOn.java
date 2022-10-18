package flattenBinaryTree;
import java.util.*;
//O(n) time complexity
//O(n) space complexity
public class flattenBinaryTreeOn {
    public static BinaryTree flattenBinaryTree(BinaryTree root) {
        //BinaryTree - A tree with left and right data fields
        List<BinaryTree> inOrder = new ArrayList<>();
        inOrderTraversal(inOrder, root);
        for (int i = 0; i < inOrder.size() - 1; i++) {
            BinaryTree t1 = inOrder.get(i);
            BinaryTree t2 = inOrder.get(i + 1);
            t1.right = t2;
            t2.left = t1;
        }
        return inOrder.get(0);
    }

    public static void inOrderTraversal(List<BinaryTree> tr, BinaryTree root) {
        if (root == null)
            return;

        if (root.left != null)
            inOrderTraversal(tr, root.left);
        tr.add(root);
        if (root.right != null)
            inOrderTraversal(tr, root.right);
        return;
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

    public static void main(String args[]){
        BinaryTree t1 = new BinaryTree(1);
        for(int i = 0; i < 20; i++){
            t1.left = new BinaryTree((int)(Math.floor(Math.random() * (25 - 1 + 1) + 1)));
            t1.right = new BinaryTree((int) (Math.floor(Math.random() * (25 - 1 + 1) + 1)));
        }
        BinaryTree t2 = flattenBinaryTree(t1);
        inOrderPrint(t2);
    }
    public static void inOrderPrint(BinaryTree t1){
        if(t1 == null)return;
        if(t1.left != null)inOrderPrint(t1.left);
        System.out.println(t1.value);
        if(t1.right != null)inOrderPrint(t1.right);
        return;
    }
}
