
class closestValueInBST {
  // avg O(log n) time O(log n) space
  // worst O(n) time O(n) space
  public static int CLOSEST = Integer.MAX_VALUE;
  public static int findClosestValueInBst(BST tree, int target) {
    if(Math.abs(target - tree.value) < Math.abs(target - CLOSEST)){
      CLOSEST = tree.value;
    }
    //if(tree == null)return CLOSEST;
    
    if(tree.value < target && tree.right != null){
      findClosestValueInBst(tree.right,target);
    }
    if(tree.value > target && tree.left != null){
      findClosestValueInBst(tree.left,target);
    }
    return CLOSEST;
  }

  static class BST {
    public int value;
    public BST left;
    public BST right;

    public BST(int value) {
      this.value = value;
    }
  }
}
