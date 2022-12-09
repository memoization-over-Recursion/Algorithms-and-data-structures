import java.util.*;
import java.util.function.BiFunction;
// Do not edit the class below except for
// the insert method. Feel free to add new
// properties and methods to the class.
public class continuosMedian {
  static class ContinuousMedianHandler {
    Heap lower = new Heap(Heap::MAX_FUNC, new ArrayList<Integer>());
    Heap higher = new Heap(Heap::MIN_FUNC, new ArrayList<Integer>());
    double median = 0;
    //time complexity O( log( n ) )
    //space complexity O( n )
    public void insert(int number) {
      if(lower.len == 0 ||  number < lower.peek() ){
        lower.insert(number);
      }else{
        higher.insert(number);
      }
      rebalance();
      update();
      System.out.println(median);
    }
    public void update(){
      if(lower.len == higher.len)
        median = ((double)lower.peek() + (double)higher.peek()) / 2;
      else if(lower.len > higher.len){
        median = lower.peek();
      }else{
         median = higher.peek();
      }
    }
    public void rebalance(){
      if(lower.len - higher.len == 2){
        higher.insert(lower.remove());
      }else if(higher.len - lower.len == 2){
        lower.insert(higher.remove());
      }
    }

    public double getMedian() {
      return median;
    }
  }
  static class Heap {
    List<Integer> heap = new ArrayList<Integer>();
    BiFunction <Integer , Integer , Boolean> comparison;
    int len;

    public Heap(BiFunction <Integer , Integer , Boolean> comparisons, List<Integer> array) {
      heap = buildHeap(array);
      comparison = comparisons;
      len = heap.size();
    }

    //time complexity O(n)
    //space complexity O(1)
    public List<Integer> buildHeap(List<Integer> array) {
      int firstParent = (array.size()-2) / 2;
      for(int current  = firstParent; current >= 0; current--){
        siftDown(current , array.size()-1 , array);
      }
      return array;
      
    }

    //time complexity O(log(n))
    //space complexity O(1)
    public void siftDown(int currentIdx, int endIdx, List<Integer> heap) {
      int childOne = currentIdx * 2 + 1;
      while(childOne <= endIdx){
        int childTwo = currentIdx*2+2 <= endIdx ? currentIdx * 2 + 2 : -1;
        int idxToSwap;
        if(childTwo != -1){
          if(comparison.apply(heap.get(childTwo), heap.get(childOne))){
          idxToSwap = childTwo;
          }else{
            idxToSwap = childOne;
          }
        }else{
          idxToSwap = childOne;
        }
          
          if(comparison.apply(heap.get(idxToSwap), heap.get(currentIdx))){
            swap(heap , idxToSwap , currentIdx);
            currentIdx = idxToSwap;
            childOne = currentIdx * 2 + 1;
          }else{
            return;
          }
      }
    }
    //time complexity O(log(n))
    //space complexity O(1)
    public void siftUp(int currentIdx, List<Integer> heap) {
      int parentIdx = ( currentIdx - 1 ) / 2;
      while(currentIdx > 0 ){
        if(comparison.apply(heap.get(currentIdx), heap.get(parentIdx))){
        swap(heap , currentIdx , parentIdx );
        currentIdx = parentIdx;
        parentIdx = ( currentIdx - 1 ) / 2;
      }else{
          return;
      }
    }
    }

    public int peek() {
      return heap.get(0);
    }

    public int remove() {
      swap(heap , 0 , heap.size() - 1 );
      int valRemoved = heap.get( heap.size() - 1 );
      heap.remove( heap.size() - 1 );
      len--;
      siftDown(0 , heap.size() - 1, heap );
      return valRemoved;
    }

    public void insert(int value) {
      heap.add(value);
      len++;
      siftUp(heap.size() - 1 , heap);
    }

    public void swap(List<Integer> heap , int a , int b){
      Integer temp = heap.get(b);
      heap.set(b , heap.get(a));
      heap.set(a , temp);
    }
    public static Boolean MIN_FUNC(Integer a , Integer b){
    return a < b;
    }
    public static Boolean MAX_FUNC(Integer a , Integer b){
    return a > b;
    }
  }
}
