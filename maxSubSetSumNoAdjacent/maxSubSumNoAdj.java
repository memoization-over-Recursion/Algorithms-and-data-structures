package maxSubSetSumNoAdjacent;
//time complexity O(n)
//space complexity O(1)
public class maxSubSumNoAdj {
    public static int maxSubSetSumNoAdjacent(int[] array){
        if(array.length == 1)return array[0];
        if(array.length == 0)return 0;

        int first = Math.max(array[0] , array[1]);
        int second = array[0];

        for(int i = 2; i < array.length; i++){
            int current = Math.max(first, second+array[i]);
            second = first;
            first = current;
        }
        return first;
    }
}

