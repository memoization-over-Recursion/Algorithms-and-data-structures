package dataStructures;

import java.util.*;

class minHeap {
    static class MinHeap {
        List<Integer> heap = new ArrayList<Integer>();

        public MinHeap(List<Integer> array) {
            heap = buildHeap(array);
        }

        // time complexity O(n)
        // space complexity O(1)
        public List<Integer> buildHeap(List<Integer> array) {
            int firstParent = (array.size() - 2) / 2;
            for (int current = firstParent; current >= 0; current--) {
                siftDown(current, array.size() - 1, array);
            }
            return array;

        }

        // time complexity O(log(n))
        // space complexity O(1)
        public void siftDown(int currentIdx, int endIdx, List<Integer> heap) {
            int childOne = currentIdx * 2 + 1;
            while (childOne <= endIdx) {
                int childTwo = currentIdx * 2 + 2 <= endIdx ? currentIdx * 2 + 2 : -1;
                int idxToSwap;
                if (childTwo != -1 && heap.get(childTwo) < heap.get(childOne)) {
                    idxToSwap = childTwo;
                } else {
                    idxToSwap = childOne;
                }
                if (heap.get(idxToSwap) < heap.get(currentIdx)) {
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
        public void siftUp(int currentIdx, List<Integer> heap) {
            int parentIdx = (currentIdx - 1) / 2;
            while (currentIdx > 0 && heap.get(currentIdx) < heap.get(parentIdx)) {
                swap(heap, currentIdx, (currentIdx - 1) / 2);
                currentIdx = parentIdx;
                parentIdx = (currentIdx - 1) / 2;
            }
        }

        public int peek() {
            return heap.get(0);
        }

        public int remove() {
            swap(heap, 0, heap.size() - 1);
            int valRemoved = heap.get(heap.size() - 1);
            heap.remove(heap.size() - 1);
            siftDown(0, heap.size() - 1, heap);
            return valRemoved;
        }

        public void insert(int value) {
            heap.add(value);
            siftUp(heap.size() - 1, heap);
        }

        public void swap(List<Integer> heap, int a, int b) {
            Integer temp = heap.get(b);
            heap.set(b, heap.get(a));
            heap.set(a, temp);
        }
    }
}
