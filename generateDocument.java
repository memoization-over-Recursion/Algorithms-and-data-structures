import java.util.*;
// time complexity O( n + m )
// space complexity O( c )
public class generateDocument {
   
    public boolean generateDocuments(String characters, String document) {
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        for (char c : characters.toCharArray()) {
            if (map.containsKey(c)) {
                map.put(c, map.get(c) + 1);
            } else {
                map.put(c, 1);
            }
        }
        for (char d : document.toCharArray()) {
            if (map.containsKey(d)) {
                if (map.get(d) == 0) {
                    return false;
                } else {
                    map.put(d, map.get(d) - 1);
                }
            } else {
                return false;
            }
        }
        return true;
    }
}
