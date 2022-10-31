package sorting;
//Best time complexity O(nlog(n))
//Best space complexity O(1)
//Worst time complexity O(nlog(n))
//Worst space complexity O(1)
//Avg time complexity O(nlog(n))
//Avg space complexity O(1)
class heapSort {
    public static int[] heapSorter(int[] array) {
        buildHeap(array);
        for (int i = array.length - 1; i > 0; i--) {
            swap(array, 0, i);
            siftDown(0, i - 1, array);
        }
        return array;
    }

    public static void buildHeap(int[] array) {
        int firstParent = (array.length - 2) / 2;
        for (int current = firstParent; current >= 0; current--) {
            siftDown(current, array.length - 1, array);
        }
    }

    public static void siftDown(int currentIdx, int endIdx, int[] heap) {
        int childOne = currentIdx * 2 + 1;
        while (childOne <= endIdx) {
            int childTwo = currentIdx * 2 + 2 <= endIdx ? currentIdx * 2 + 2 : -1;
            int idxToSwap;
            if (childTwo != -1 && heap[childTwo] > heap[childOne]) {
                idxToSwap = childTwo;
            } else {
                idxToSwap = childOne;
            }
            if (heap[idxToSwap] > heap[currentIdx]) {
                swap(heap, idxToSwap, currentIdx);
                currentIdx = idxToSwap;
                childOne = currentIdx * 2 + 1;
            } else {
                return;
            }
        }
    }

    public static void swap(int[] heap, int a, int b) {
        int temp = heap[a];
        heap[a] = heap[b];
        heap[b] = temp;
    }

}
