import javax.crypto.*;
import javax.crypto.spec.SecretKeySpec;

public class DES {
    public static void main(String[] args) throws Exception {
        String msg = "Hello";
        byte[] keyBytes = "12345678".getBytes();
        SecretKey key = new SecretKeySpec(keyBytes, "DES");

        Cipher c = Cipher.getInstance("DES");
        c.init(Cipher.ENCRYPT_MODE, key);
        byte[] enc = c.doFinal(msg.getBytes());

        c.init(Cipher.DECRYPT_MODE, key);
        byte[] dec = c.doFinal(enc);

        for (byte b : enc) System.out.printf("%02x", b);
        System.out.println();
        System.out.println(new String(dec));
    }
}
