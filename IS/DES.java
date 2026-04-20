import javax.crypto.*;
import javax.crypto.spec.SecretKeySpec;
import java.util.Base64;

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

        System.out.println(Base64.getEncoder().encodeToString(enc));
        System.out.println(new String(dec));
    }
}
