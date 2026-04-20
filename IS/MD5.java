import java.security.*;

public class MD5 {
    public static void main(String[] args) throws Exception {
        String msg = "Hello";
        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] hash = md.digest(msg.getBytes());

        for (byte b : hash)
            System.out.printf("%02x", b);
    }
}
