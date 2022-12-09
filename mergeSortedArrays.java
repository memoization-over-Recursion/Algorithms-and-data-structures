import java.util.*;

public class mergeSortedArrays {
    // time complexity O( nlog( k ) + k )
    // space complexity O( n + k )
    public static List<Integer> mergeSortedArray(List<List<Integer>> arrays) {
        List<Integer> sortedList = new ArrayList<Integer>();
        List<Item> items = new ArrayList<Item>();
        for (int i = 0; i < arrays.size(); i++) {
            items.add(new Item(i, 0, arrays.get(i).get(0)));
        }
        MinHeap heap = new MinHeap(items);

        while (!heap.isEmpty()) {
            Item removedItem = heap.remove();
            sortedList.add(removedItem.val);
            if (removedItem.id2 == arrays.get(removedItem.id).size() - 1)
                continue;
            heap.insert(
                    new Item(removedItem.id, removedItem.id2 + 1, arrays.get(removedItem.id).get(removedItem.id2 + 1)));
        }
        return sortedList;
    }

    static class Item {
        public int id;
        public int id2;
        public int val;

        public Item(int id, int id2, int val) {
            this.id = id;
            this.id2 = id2;
            this.val = val;
        }

    }

    static class MinHeap {
        List<Item> heap = new ArrayList<Item>();

        public MinHeap(List<Item> array) {
            heap = buildHeap(array);
        }

        // time complexity O(n)
        // space complexity O(1)
        public List<Item> buildHeap(List<Item> array) {
            int firstParent = (array.size() - 2) / 2;
            for (int current = firstParent; current >= 0; current--) {
                siftDown(current, array.size() - 1, array);
            }
            return array;

        }

        // time complexity O(log(n))
        // space complexity O(1)
        public void siftDown(int currentIdx, int endIdx, List<Item> heap) {
            int childOne = currentIdx * 2 + 1;
            while (childOne <= endIdx) {
                int childTwo = currentIdx * 2 + 2 <= endIdx ? currentIdx * 2 + 2 : -1;
                int idxToSwap;
                if (childTwo != -1 && heap.get(childTwo).val < heap.get(childOne).val) {
                    idxToSwap = childTwo;
                } else {
                    idxToSwap = childOne;
                }
                if (heap.get(idxToSwap).val < heap.get(currentIdx).val) {
                    Collections.swap(heap, idxToSwap, currentIdx);
                    currentIdx = idxToSwap;
                    childOne = currentIdx * 2 + 1;
                } else {
                    return;
                }
            }
        }

        // time complexity O(log(n))
        // space complexity O(1)
        public void siftUp(int currentIdx, List<Item> heap) {
            int parentIdx = (currentIdx - 1) / 2;
            while (currentIdx > 0 && heap.get(currentIdx).val < heap.get(parentIdx).val) {
                swap(heap, currentIdx, (currentIdx - 1) / 2);
                currentIdx = parentIdx;
                parentIdx = (currentIdx - 1) / 2;
            }
        }

        public Item peek() {
            return heap.get(0);
        }

        public Item remove() {
            swap(heap, 0, heap.size() - 1);
            Item valRemoved = heap.get(heap.size() - 1);
            heap.remove(heap.size() - 1);
            siftDown(0, heap.size() - 1, heap);
            return valRemoved;
        }

        public boolean isEmpty() {
            return heap.size() == 0;
        }

        public void insert(Item value) {
            heap.add(value);
            siftUp(heap.size() - 1, heap);
        }

        public void swap(List<Item> heap, int a, int b) {
            Item temp = heap.get(b);
            heap.set(b, heap.get(a));
            heap.set(a, temp);
        }
    }
}
