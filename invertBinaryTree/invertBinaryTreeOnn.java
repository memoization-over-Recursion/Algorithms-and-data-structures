package invertBinaryTree;
import java.util.ArrayDeque;

class invertBinaryTreeOnn {
    public static void invertBinaryTree(BinaryTree tree){
        ArrayDeque<BinaryTree> queue = new ArrayDeque<BinaryTree>();
        queue.addLast(tree);
        while(queue.size() > 0){
            BinaryTree current = queue.pollFirst();
            swapLeftandRight(current);
            if(current.left != null){
                queue.addLast(current.left);
            }
            if (current.right != null) {
                queue.addLast(current.right);
            }
        }
    }
    public static void swapLeftandRight(BinaryTree tree){
        BinaryTree left = tree.left;
        tree.left = tree.right;
        tree.right = left;
    }
    
    class BinaryTree {
        public int value;
        public BinaryTree left;
        public BinaryTree right;

        public BinaryTree(int val) {
            this.value = val;
        }
    }
}
/*
                1
               / \
              3   2
             / \ / \
            4  5 6  7

we take tree at 3 and 2 and we swap them

                1
               / \
              2   3
             / \ / \
            6  7 4  5

we take tree at 6,7 and 4,5 and swap 

                1
               / \
              2   3
             / \ / \
            7  6 5  4

*/