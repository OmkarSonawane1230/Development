#include <iostream>
#include <openssl/des.h>
#include <cstring>

using namespace std;

int main() {
    DES_cblock key = { '1','2','3','4','5','6','7','8' };
    DES_cblock msg = { 'H','e','l','l','o',' ',' ',' ' };
    DES_cblock enc, dec;
    DES_key_schedule schedule;

    DES_set_key_unchecked(&key, &schedule);
    DES_ecb_encrypt(&msg, &enc, &schedule, DES_ENCRYPT);
    DES_ecb_encrypt(&enc, &dec, &schedule, DES_DECRYPT);

    for(int i=0; i<8; i++) printf("%02x", enc[i]);
    cout << "\n" << dec << endl;

    return 0;
}
// Compile with: g++ DES.cpp -lssl -lcrypto
