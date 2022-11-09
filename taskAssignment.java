import java.util.*;
// time complexity O( nlog(n) )
// space complexity O( n )
class taskAssignment {

    public ArrayList<ArrayList<Integer>> taskAssignments(int k, ArrayList<Integer> tasks) {
        HashMap<Integer, ArrayList<Integer>> map = makeHashMap(tasks);

        List<Integer> sorted = tasks;
        Collections.sort(sorted);
        ArrayList<ArrayList<Integer>> answer = new ArrayList<ArrayList<Integer>>();
        for (int j = 0; j < k; j++) {
            ArrayList<Integer> taskAssignment = new ArrayList<Integer>();
            int smallest = sorted.get(j);
            ArrayList<Integer> task1Indices = map.get(smallest);
            int indices1 = task1Indices.remove(task1Indices.size() - 1);
            int largest = sorted.get(tasks.size() - 1 - j);
            ArrayList<Integer> task2Indices = map.get(largest);
            int indices2 = task2Indices.remove(task2Indices.size() - 1);
            taskAssignment.add(indices1);
            taskAssignment.add(indices2);
            answer.add(taskAssignment);

        }
        return answer;
    }

    public static HashMap<Integer, ArrayList<Integer>> makeHashMap(ArrayList<Integer> tasks) {
        HashMap<Integer, ArrayList<Integer>> mapToBeReturned = new HashMap<Integer, ArrayList<Integer>>();

        for (int i = 0; i < tasks.size(); i++) {
            int valueToBeAdded = tasks.get(i);
            if (mapToBeReturned.containsKey(valueToBeAdded)) {
                mapToBeReturned.get(valueToBeAdded).add(i);
            } else {
                ArrayList<Integer> arToBeAdded = new ArrayList<Integer>();
                arToBeAdded.add(i);
                mapToBeReturned.put(valueToBeAdded, arToBeAdded);
            }
        }
        return mapToBeReturned;
    }
}
