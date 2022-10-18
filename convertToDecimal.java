public class convertToDecimal {
   public static void main(String args[]){
    String bin = "10110";
    int decimal = binaryToDecimal(bin);
    System.out.println(decimal);
   } 
   public static int binaryToDecimal(String bin){
       int conversion = 1;
       int result = 0;
       for(int i = bin.length()-1; i >= 0; i--){
           if(bin.charAt(i) == '1'){
               result += conversion;
           }
           conversion *= 2;
       }
       return result;
   }


}
