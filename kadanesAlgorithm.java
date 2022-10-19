// time complexity O(n)
// space complexity O(1)
public class kadanesAlgorithm {
   public static int kadaneAlgorithm(int[] ar){
       int previousGreatest = ar[0];
       int currentGreatest = ar[0];
       for(int i = 1; i < ar.length; i++){
           int cNum = ar[i];
           previousGreatest = Math.max(previousGreatest+cNum , cNum );
           currentGreatest = Math.max(currentGreatest,previousGreatest);
       }
       return currentGreatest;
   }
}
