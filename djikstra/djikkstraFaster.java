package djikstra;
import java.util.*;
// time complexity O( (v + e) * log( v ) )
// space complexity O( v )
public class djikkstraFaster {
    public int[] dijkstrasAlgorithm(int start, int[][][] edges) {
        int size = edges.length;
        int[] min = new int[size];
        Arrays.fill(min, Integer.MAX_VALUE);
        min[start] = 0;

        List<Item> minDistance = new ArrayList<Item>();
        for (int i = 0; i < size; i++) {
            Item item = new Item(i, Integer.MAX_VALUE);
            minDistance.add(item);
        }

        MinHeap minim = new MinHeap(minDistance);
        minim.update(start, 0);

        while (!minim.isEmpty()) {
            Item i = minim.remove();
            int vertex = i.vertex;
            int distance = i.distance;

            if (distance == Integer.MAX_VALUE) {
                break;
            }
            for (int[] edge : edges[vertex]) {
                int destin = edge[0];
                int distToDest = edge[1];
                int newPath = distance + distToDest;
                int currentDest = min[destin];
                if (newPath < currentDest) {
                    min[destin] = newPath;
                    minim.update(destin, newPath);
                }
            }
        }
        int[] finalDist = new int[min.length];
        for (int i = 0; i < min.length; i++) {
            if (min[i] == Integer.MAX_VALUE) {
                finalDist[i] = -1;
            } else {
                finalDist[i] = min[i];
            }
        }

        return finalDist;
    }

    static class Item {
        int vertex;
        int distance;

        public Item(int vertex, int distance) {
            this.vertex = vertex;
            this.distance = distance;
        }
    }

    static class MinHeap {
        Map<Integer, Integer> vertexMap = new HashMap<Integer, Integer>();
        List<Item> heap = new ArrayList<Item>();

        public MinHeap(List<Item> array) {
            for (int i = 0; i < array.size(); i++) {
                Item item = array.get(i);
                vertexMap.put(item.vertex, item.vertex);
            }
            heap = buildHeap(array);
        }

        // time complexity O(n)
        // space complexity O(1)
        List<Item> buildHeap(List<Item> array) {
            int firstParent = (array.size() - 2) / 2;
            for (int current = firstParent; current >= 0; current--) {
                siftDown(current, array.size() - 1, array);
            }
            return array;

        }

        // time complexity O(log(n))
        // space complexity O(1)
        void siftDown(int currentIdx, int endIdx, List<Item> heap) {
            int childOne = currentIdx * 2 + 1;
            while (childOne <= endIdx) {
                int childTwo = currentIdx * 2 + 2 <= endIdx ? currentIdx * 2 + 2 : -1;
                int idxToSwap;
                if (childTwo != -1 && heap.get(childTwo).distance < heap.get(childOne).distance) {
                    idxToSwap = childTwo;
                } else {
                    idxToSwap = childOne;
                }
                if (heap.get(idxToSwap).distance < heap.get(currentIdx).distance) {
                    swap(idxToSwap, currentIdx);
                    currentIdx = idxToSwap;
                    childOne = currentIdx * 2 + 1;
                } else {
                    return;
                }
            }
        }

        // time complexity O(log(n))
        // space complexity O(1)
        public void siftUp(int currentIdx) {
            int parentIdx = (currentIdx - 1) / 2;
            while (currentIdx > 0 && heap.get(currentIdx).distance < heap.get(parentIdx).distance) {
                swap(currentIdx, (currentIdx - 1) / 2);
                currentIdx = parentIdx;
                parentIdx = (currentIdx - 1) / 2;
            }
        }

        Item remove() {
            if (isEmpty()) {
                return null;
            }
            swap(0, heap.size() - 1);
            Item valRemoved = heap.get(heap.size() - 1);
            int vertex = valRemoved.vertex;
            int distance = valRemoved.distance;
            heap.remove(heap.size() - 1);
            siftDown(0, heap.size() - 1, heap);
            return new Item(vertex, distance);
        }

        boolean isEmpty() {
            return heap.size() == 0;
        }

        void update(int vertex, int value) {
            heap.set(vertexMap.get(vertex), new Item(vertex, value));
            siftUp(vertexMap.get(vertex));
        }

        public void swap(int a, int b) {
            vertexMap.put(heap.get(a).vertex, b);
            vertexMap.put(heap.get(b).vertex, a);
            Item temp = heap.get(b);
            heap.set(b, heap.get(a));
            heap.set(a, temp);
        }
    }
}
