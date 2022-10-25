package sorting;

// best time O(n^2) / space O(1)
// average O(N^2) / O(1) space
// Worst O(n^2) / O(1) space
public class selectionSort {

    public static int[] selectSort(int[] ar){
        for(int i = 0; i < ar.length; i++){
            int iOfSmall = 0;
            int smallest = Integer.MAX_VALUE;
            for(int j = i; j < ar.length; j++){
                if(smallest > ar[j]){
                    smallest = Math.min(smallest , ar[j]);
                    iOfSmall = j;
                }
            }
            swap(ar , i , iOfSmall);
        }
        return ar;
    }

    public static void swap(int[] ar , int a, int b){
        int temp = ar[a];
        ar[a] = ar[b];
        ar[b] = temp;
    }
}
