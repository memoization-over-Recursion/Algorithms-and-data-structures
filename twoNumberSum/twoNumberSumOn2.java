package twoNumberSum;

public class twoNumberSumOn2 {
  //O(n^2) time complexity
  //O(1) space complexity
  public static int[] twoNumberSum(int[] array, int targetSum) {
   // array - distinct integer array ( no two ints are the same )
   // targetSum - distinct non negative integer value
   for(int i = 0; i < array.length; i++){
     for(int j = array.length-1; j >= 0 ; j--){
       if(i != j && array[i] + array[j] == targetSum){
         return new int[]{array[i] , array[j]};
       }
     }
   }
    return new int[]{};
  }
  public static void main(String args[]){
    int[] array = new int[]{2,1,3,4,5,6,9};
    System.out.println(twoNumberSum(array,15)[0]);
  }
}
