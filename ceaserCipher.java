// time complexity O( n )
// space complexity O( n )
public class ceaserCipher {
    public static String caesarCypherEncryptor(String str, int key) {
        StringBuilder s = new StringBuilder();
        int cd = key % 26;
        for (char c : str.toCharArray()) {
            if (c + cd <= 122) {
                s.append((char) (c + cd));
            } else {
                int start = (c + cd) - 'a';
                start %= 26;
                start += 'a';
                s.append((char) start);
            }

        }
        return s.toString();

    }
}