package firstDuplicateValue;
//time complexity O( n )
//space complexity O( 1 )
class firstDuplicateValueArray {
    
    public int firstDuplicateValue(int[] array) {
        for (int i : array) {
            if (array[Math.abs(i) - 1] < 0)
                return Math.abs(i);
            array[Math.abs(i) - 1] *= -1;
        }
        return -1;
    }
}
