#include <iostream>
#include <string>

using namespace std;

string encrypt(string s, int key) {
    string res = "";
    for (int i = 0; i < key; i++)
        for (int j = i; j < s.length(); j += key)
            res += s[j];
    return res;
}

string decrypt(string s, int key) {
    string res = s;
    int k = 0;
    for (int i = 0; i < key; i++)
        for (int j = i; j < s.length(); j += key)
            res[j] = s[k++];
    return res;
}

int main() {
    string msg = "HELLOWORLD";
    string enc = encrypt(msg, 3);
    cout << enc << endl;
    cout << decrypt(enc, 3) << endl;
    return 0;
}
