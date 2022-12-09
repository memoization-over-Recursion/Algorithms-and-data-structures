import java.util.*;

public class laptopRentals {
  //time complexity O( nlog( n ) )
  //space complexity O( n )
  public int laptopRental(ArrayList<ArrayList<Integer>> times) {
    if(times.size() == 0)return 0;


    Collections.sort(times , (a,b) -> Integer.compare(a.get(0) , b.get(0)));
    ArrayList<ArrayList<Integer>> timesForLaptop = new ArrayList<ArrayList<Integer>>();
    timesForLaptop.add(times.get(0));
    MinHeap heap = new MinHeap(timesForLaptop);
    for(int i = 1 ; i < times.size(); i++){
      if(heap.peek().get(1) <= times.get(i).get(0)){
        heap.remove();
      }
      heap.insert(times.get(i));
    }
    return timesForLaptop.size();
  }


  
  static class MinHeap {
    List<ArrayList<Integer>> heap = new ArrayList<ArrayList<Integer>>();

    public MinHeap(List<ArrayList<Integer>> array) {
      heap = buildHeap(array);
    }

    //time complexity O(n)
    //space complexity O(1)
    public List<ArrayList<Integer>> buildHeap(List<ArrayList<Integer>> array) {
      int firstParent = (array.size()-2) / 2;
      for(int current  = firstParent; current >= 0; current--){
        siftDown(current , array.size()-1 , array);
      }
      return array;
      
    }

    //time complexity O(log(n))
    //space complexity O(1)
    public void siftDown(int currentIdx, int endIdx, List<ArrayList<Integer>> heap) {
      int childOne = currentIdx * 2 + 1;
      while(childOne <= endIdx){
        int childTwo = currentIdx*2+2 <= endIdx ? currentIdx * 2 + 2 : -1;
        int idxToSwap;
        if(childTwo != -1 && heap.get(childTwo).get(1) < heap.get(childOne).get(1)){
          idxToSwap = childTwo;
        }else{
          idxToSwap = childOne;
        }
          if(heap.get(idxToSwap).get(1) < heap.get(currentIdx).get(1)){
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
    public void siftUp(int currentIdx, List<ArrayList<Integer>> heap) {
      int parentIdx = ( currentIdx - 1 ) / 2;
        while(currentIdx > 0 && heap.get(currentIdx).get(1) < heap.get(parentIdx).get(1)){
        swap(heap , currentIdx , ( currentIdx - 1 ) / 2 );
        currentIdx = parentIdx;
        parentIdx = ( currentIdx - 1 ) / 2;
      }
    }

    public ArrayList<Integer> peek() {
      return heap.get(0);
    }

    public List<Integer> remove() {
      swap(heap , 0 , heap.size() - 1 );
      ArrayList<Integer> valRemoved = heap.get( heap.size() - 1 );
      heap.remove( heap.size() - 1 );
      siftDown(0 , heap.size() - 1, heap );
      return valRemoved;
    }

    public void insert(ArrayList<Integer> value) {
      heap.add(value);
      siftUp(heap.size()-1 , heap);
    }

    public void swap(List<ArrayList<Integer>> heap , int a , int b){
      ArrayList<Integer> temp = heap.get(b);
      heap.set(b , heap.get(a));
      heap.set(a , temp);
    }
  }
}
