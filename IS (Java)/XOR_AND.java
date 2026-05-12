public class XOR_AND {
    public static void main(String[] args) {
        String s = "Hello\nWorld";

        for (char c : s.toCharArray())
            System.out.print((char)(c ^ 127));

        System.out.println();

        for (char c : s.toCharArray())
            System.out.print((char)(c & 127));
    }
}
