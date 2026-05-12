#include <iostream>
#include <openssl/md5.h>
#include <iomanip>

using namespace std;

int main() {
    string msg = "Hello";
    unsigned char hash[MD5_DIGEST_LENGTH];

    MD5((unsigned char*)msg.c_str(), msg.length(), hash);

    for(int i = 0; i < MD5_DIGEST_LENGTH; i++)
        cout << hex << setw(2) << setfill('0') << (int)hash[i];
    cout << endl;

    return 0;
}
// Compile with: g++ MD5.cpp -lssl -lcrypto
