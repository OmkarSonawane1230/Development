#include <iostream>
#include <openssl/aes.h>

using namespace std;

int main() {
    unsigned char key[16] = "123456789012345";
    unsigned char msg[16] = "Hello          ";
    unsigned char enc[16], dec[16];

    AES_KEY enc_key, dec_key;
    AES_set_encrypt_key(key, 128, &enc_key);
    AES_encrypt(msg, enc, &enc_key);

    AES_set_decrypt_key(key, 128, &dec_key);
    AES_decrypt(enc, dec, &dec_key);

    for(int i=0; i<16; i++) printf("%02x", enc[i]);
    cout << "\n" << dec << endl;

    return 0;
}
// Compile with: g++ AES.cpp -lssl -lcrypto
