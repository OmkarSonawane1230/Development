import java.security.*;
import javax.crypto.Cipher;

public class RSA {
    public static void main(String[] args) throws Exception {
        String msg = "Hello";

        KeyPairGenerator kpg = KeyPairGenerator.getInstance("RSA");
        kpg.initialize(512);
        KeyPair kp = kpg.generateKeyPair();

        Cipher c = Cipher.getInstance("RSA");

        c.init(Cipher.ENCRYPT_MODE, kp.getPublic());
        byte[] enc = c.doFinal(msg.getBytes());

        c.init(Cipher.DECRYPT_MODE, kp.getPrivate());
        byte[] dec = c.doFinal(enc);

        System.out.println(new String(dec));
    }
}
