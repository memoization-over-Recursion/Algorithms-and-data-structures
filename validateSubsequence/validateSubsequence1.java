package validateSubsequence;
import java.util.*;
//time complexity O(n)
//space complexity O(1)
public class validateSubsequence1{
public static boolean isValidSubsequence(List<Integer> array , List<Integer> sequence){
    int sequenceIdx = 0;
    for(int arIdx = 0; arIdx < array.size() && sequenceIdx < sequence.size();){
        if(sequenceIdx == sequence.size())break;
        
        if(array.get(arIdx) == sequence.get(sequenceIdx)){
            sequenceIdx++;
        }
        arIdx++;
    }
    return sequenceIdx == sequence.size();
}
}