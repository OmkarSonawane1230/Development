public class Transposition {
    static String encrypt(String s, int key) {
        String res = "";
        for (int i = 0; i < key; i++)
            for (int j = i; j < s.length(); j += key)
                res += s.charAt(j);
        return res;
    }

    static String decrypt(String s, int key) {
        char[] res = new char[s.length()];
        int k = 0;
        for (int i = 0; i < key; i++)
            for (int j = i; j < s.length(); j += key)
                res[j] = s.charAt(k++);
        return new String(res);
    }

    public static void main(String[] args) {
        String msg = "HELLOWORLD";
        String enc = encrypt(msg, 3);
        System.out.println(enc);
        System.out.println(decrypt(enc, 3));
    }
}
