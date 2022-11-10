import java.util.*;
//time complexity O( n^3 + m )
//space complexity O( n + m )
class numbersInPi {
    public static int numbersinpi(String pi, String[] numbers) {
        Set<String> map = new HashSet<String>();
        for (String num : numbers)
            map.add(num);
        HashMap<Integer, Integer> cache = new HashMap<Integer, Integer>();
        int min = getSpaces(pi, cache, map, 0);
        return min == Integer.MAX_VALUE ? -1 : min;
    }

    public static int getSpaces(String pi, Map<Integer, Integer> cache, Set<String> map, int id) {
        if (id == pi.length())
            return -1;
        if (cache.containsKey(id))
            return cache.get(id);
        int minSpaces = Integer.MAX_VALUE;
        for (int i = id; i < pi.length(); i++) {
            String sub = pi.substring(id, i + 1);
            if (map.contains(sub)) {
                int newNum = getSpaces(pi, cache, map, i + 1);
                if (newNum == Integer.MAX_VALUE) {
                    minSpaces = Math.min(newNum, minSpaces);
                } else {
                    minSpaces = Math.min(newNum + 1, minSpaces);
                }
            }
        }
        cache.put(id, minSpaces);
        return cache.get(id);
    }
}
