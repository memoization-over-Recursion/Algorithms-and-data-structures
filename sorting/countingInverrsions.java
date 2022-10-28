package sorting;
import java.util.*;
//time complexity O( nlog(n) )
//space complexity O( n )
class countingInverrsions {

    public int countInversions(int[] array) {
        return countInversions(array, 0, array.length);
    }

    public int countInversions(int[] ar, int start, int end) {
        if (end - start <= 1)
            return 0;

        int middle = start + (end - start) / 2;
        int leftInversions = countInversions(ar, start, middle);
        int rightInversions = countInversions(ar, middle, end);
        int mergedInversions = mergeAndCountInversions(ar, start, middle, end);

        return leftInversions + rightInversions + mergedInversions;

    }

  public int mergeAndCountInversions(int[] ar , int start , int middle , int end){
    List<Integer> arr = new ArrayList<Integer>();
    int left = start;
    int right = middle;
    int inversions = 0;
    while(left < middle && right < end){

      if(ar[left] <= ar[right]){
        arr.add(ar[left++]);
      }else{
        inversions += (middle - left);
        arr.add(ar[right++]);
      }
    }
    int i = left;
    while(i < middle){
      arr.add(ar[i++]);
    }
    int j = right;
    while(j < right){
      arr.add(ar[j++]);
    }

    int k = 0;
    while( k < arr.size() ){
      ar[start+k] = arr.get(k);
      k++;
    }

    return inversions;
  }
}