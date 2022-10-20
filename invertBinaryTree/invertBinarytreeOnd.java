package invertBinaryTree;
//time complexity O(n)
//space complexity O(d)
class invertBinaryTreeOnd{
    public static void invertBinaryTree(BinaryTree tree){
        if(tree == null){
            return;
        }
        BinaryTree t1 = tree.left;
        BinaryTree t2 = tree.right;
        tree.left = t1;
        tree.right = t2;
        invertBinaryTree(tree.left);
        invertBinaryTree(tree.right);
    }
}
class BinaryTree{
    public int value;
    public BinaryTree left;
    public BinaryTree right;

    public BinaryTree(int val){
        this.value = val;
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