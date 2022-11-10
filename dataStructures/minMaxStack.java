package dataStructures;
import java.util.*;

public class minMaxStack {
    static class MinMaxStack {
        List<Map<String, Integer>> minMax = new ArrayList<Map<String, Integer>>();
        List<Integer> stack = new ArrayList<Integer>();

        // time complexity O( 1 )
        // space complexity O( 1 )
        public int peek() {
            return stack.get(stack.size() - 1);
        }

        // time complexity O( 1 )
        // space complexity O( 1 )
        public int pop() {
            minMax.remove(minMax.size() - 1);
            return stack.remove(stack.size() - 1);

        }

        // time complexity O( 1 )
        // space complexity O( 1 )
        public void push(Integer number) {
            Map<String, Integer> newMinMax = new HashMap<String, Integer>();
            newMinMax.put("min", number);
            newMinMax.put("max", number);
            if (minMax.size() > 0) {
                Map<String, Integer> oldMinMax = new HashMap<String, Integer>(minMax.get(minMax.size() - 1));
                newMinMax.replace("min", Math.min(oldMinMax.get("min"), number));
                newMinMax.replace("max", Math.max(oldMinMax.get("max"), number));
            }
            minMax.add(newMinMax);
            stack.add(number);
        }

        // time complexity O( 1 )
        // space complexity O( 1 )
        public int getMin() {
            return minMax.get(minMax.size() - 1).get("min");
        }

        // time complexity O( 1 )
        // space complexity O( 1 )
        public int getMax() {
            return minMax.get(minMax.size() - 1).get("max");
        }
    }
}
