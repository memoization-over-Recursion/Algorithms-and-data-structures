import java.util.*;
public class insertionSort {
    // best time O(n) / space O(1)
    // average O(N^2) / O(1) space
    // Worst O(n^2) / O(1) space
public static int[] insSort(int[] ar){
    for(int i = 0; i < ar.length; i++){
        int key = ar[i];
        int j = i-1;
        while(j >= 0 && ar[j] > key){
            ar[j+1] = ar[j];
            j = j-1;
        }
        ar[j+1] = key;
    }
    return ar;
}
}
