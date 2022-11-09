// time complexity O( n )
// space complexity O( n )
class Program {
    public String runLengthEncoding(String string) {
        StringBuilder finalString = new StringBuilder();
        int curren = 1;
        for (int i = 1; i < string.length(); i++) {
            char current = string.charAt(i);
            char prev = string.charAt(i - 1);
            if (curren == 9 || current != prev) {
                finalString.append(curren);
                finalString.append(prev);
                curren = 0;
            }
            curren++;

        }
        finalString.append(curren);
        finalString.append(string.charAt(string.length() - 1));

        return finalString.toString();
    }
}
