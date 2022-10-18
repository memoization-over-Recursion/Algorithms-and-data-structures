public class octalToDecimal {
    public static void main(String args[]) {
        String oct = "17";
        int decimal = convertToDecimal(oct);
        System.out.println(decimal);
    }

    public static int convertToDecimal(String oct) {
        int conversion = 1;
        int result = 0;
        for (int i = oct.length()-1; i >= 0; i--) {
            result+= (Integer.parseInt(oct.charAt(i)+"")*conversion);
            conversion*=8;
        }
        return result;
    }

}
//17

