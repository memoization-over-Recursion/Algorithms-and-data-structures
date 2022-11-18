package tournamentWinner;
import java.util.*;

// time complexity O( n )
// space complexity O( k )
public class tournamentWinnerSlow {

  public String tournamentWinner(
      ArrayList<ArrayList<String>> competitions, ArrayList<Integer> results) {
    HashMap<String , Integer> map = new HashMap<String , Integer>();
      for(int i = 0; i < results.size(); i++){
        if(results.get(i) == 1){
          if(map.containsKey(competitions.get(i).get(0))){
          map.put(competitions.get(i).get(0), map.get(competitions.get(i).get(0))+3);
        }else{
          map.put(competitions.get(i).get(0), 3);
        }
        }
        else{
           if(map.containsKey(competitions.get(i).get(1))){
          map.put(competitions.get(i).get(1), map.get(competitions.get(i).get(1))+3);
        }else{
          map.put(competitions.get(i).get(1), 3);
        }
        }

        
        
      }
   
   return map.entrySet().stream().max((entry1, entry2) -> entry1.getValue() > entry2.getValue() ? 1 : -1).get().getKey();
  }
}