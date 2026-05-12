import javax.crypto.*;
import javax.crypto.spec.SecretKeySpec;

public class AES {
    public static void main(String[] args) throws Exception {
        String msg = "Hello";
        byte[] keyBytes = "1234567890123456".getBytes();
        SecretKey key = new SecretKeySpec(keyBytes, "AES");

        Cipher c = Cipher.getInstance("AES");
        c.init(Cipher.ENCRYPT_MODE, key);
        byte[] enc = c.doFinal(msg.getBytes());

        c.init(Cipher.DECRYPT_MODE, key);
        byte[] dec = c.doFinal(enc);

        for (byte b : enc) System.out.printf("%02x", b);
        System.out.println();
        System.out.println(new String(dec));
    }
}
