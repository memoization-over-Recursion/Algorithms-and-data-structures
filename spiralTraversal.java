import java.util.*;
// time complexity O( n )
// space complexity O( n )
public class spiralTraversal {
  public static List<Integer> spiralTraverse(int[][] array) {
    if(array.length == 0)return new ArrayList<Integer>();
    int sC = 0;
    int eC = array[0].length-1;
    int sR = 0;
    int eR = array.length-1;
    List<Integer> ar = new ArrayList<>();
    while(sC <= eC && sR <= eR){
      
      for(int col = sC; col <= eC; col++){
        ar.add(array[sR][col]);
      }
      for(int row = sR+1; row <= eR; row++){
        ar.add(array[row][eC]);
      }
      for(int fCol = eC-1; fCol >= sC; fCol--){
        if(sR == eR)break;
        ar.add(array[eR][fCol]);
      }
      for(int fRow = eR-1; fRow > sR; fRow--){
         if(sC == eC)break;
        ar.add(array[fRow][sC]);
      }
      
      
      sC++;
      eC--;
      sR++;
      eR--;
    }
    return ar;
}
}