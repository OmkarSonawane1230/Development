#include <iostream>
#include <openssl/rsa.h>
#include <openssl/pem.h>

using namespace std;

int main() {
    const char* msg = "Hello";
    unsigned char enc[256], dec[256];

    RSA* rsa = RSA_generate_key(512, RSA_F4, NULL, NULL);

    int enc_len = RSA_public_encrypt(strlen(msg), (unsigned char*)msg, enc, rsa, RSA_PKCS1_PADDING);
    int dec_len = RSA_private_decrypt(enc_len, enc, dec, rsa, RSA_PKCS1_PADDING);
    dec[dec_len] = '\0';

    cout << dec << endl;

    RSA_free(rsa);
    return 0;
}
// Compile with: g++ RSA.cpp -lssl -lcrypto
