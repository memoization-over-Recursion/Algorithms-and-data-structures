package sorting;
//time complexity O(n^2)
//space complexity O(1)

public class bubbleSort {
    public static int[] bubbleSorter(int[] ar){
        for(int i = 0; i < ar.length; i++){
            for(int j = 0; j < i; j++){
                if(ar[i] < ar[j]){
                    swap(i,j,ar);
                }
            }
        }
        return ar;
    }
    public static void swap(int a , int b , int[] arr){
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }
}
