#include <iostream>
#include <string>

using namespace std;

int main() {
    string s = "Hello\nWorld";

    for (char c : s)
        cout << (char)(c ^ 127);
    cout << endl;

    for (char c : s)
        cout << (char)(c & 127);
    cout << endl;

    return 0;
}
