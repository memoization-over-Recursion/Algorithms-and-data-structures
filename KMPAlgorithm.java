import java.util.*;

public class KMPAlgorithm{
  public static boolean knuthMorrisPrattAlgorithm(String string, String substring) {
     int i = 0;
     int j = 0;
     int[] KMParray = KMPArray(substring);
     while( i < string.length() ){
        if(string.charAt(i) == string.charAt(j)){
            if(j == substring.length()-1)return true;
            i++;
            j++;
        }
        else if(j > 0){
            j = KMParray[j-1]+1;
        }else{
            i++;
        }
     }
     return false;
  }
  public static int[] KMPArray(String string){
      int i = 1;
      int j = 0;
      int[] freq = new int[string.length()];
      Arrays.fill(freq , -1);
      while(i < string.length()){
          if(string.charAt(i) == string.charAt(j)){
              freq[i] = j;
              i++;
              j++;
          }
          else if(j > 0){
              j = freq[j-1]+1;
          }
          else{
              i++;
          }
      }
      return freq;

  }
}
