//time complexity O( n )
//space complexity O( h )
class nodeDepths{
public static int a = 0;
  public static int nodeDepth(BinaryTree root) {
    return helper(root, 0);
  }
  public static int helper(BinaryTree root, int running){
    if(root == null)return 0;
    return running + helper(root.left, running+1)+ helper(root.right, running+1);
  }

  static class BinaryTree {
    int value;
    BinaryTree left;
    BinaryTree right;

    public BinaryTree(int value) {
      this.value = value;
      left = null;
      right = null;
    }
  }
}
