package sorting;
import java.util.*;
//time complexity O(d*(n+b))
//space complexity O(n+b)
public class radixSort {

    public ArrayList<Integer> radixSort1(ArrayList<Integer> array){
        if(array.size() == 0)return array;

        int max = Collections.max(array);
        int digitInNumber = 0;
        while(( max / Math.pow( 10 , digitInNumber )) > 0){
            countingSort(array,digitInNumber);
            digitInNumber++;
        }
        return array;
    }

    public static void countingSort(List<Integer> ar , int digitInNumber){

        int[] count = new int[10];
        int[] answer = new int[ar.size()];
        int digits = (int)Math.pow(10 , digitInNumber);

        for(int n : ar){
            int idx = ( n / digits ) % 10;
            count[ idx ]++;
        }

        for(int i = 1; i < 10; i++){
            count[ i ] += count[ i - 1 ];
        }

        for(int j = ar.size()-1; j >= 0; j--){
            int cI = (ar.get(j) / digitInNumber) % 10;
            count[cI]++;
            int sortId = count[cI];
            answer[ sortId ] = ar.get(j);
        }

        for(int k = 0; k < ar.size(); k++){
            ar.set(k , answer[k]);
        }

    }
}
