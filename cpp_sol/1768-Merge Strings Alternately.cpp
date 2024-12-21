#include <iostream>
using namespace std;
string mergeAlternately(string word1, string word2) {
    string word3 ="";
    const int minLen =min( word1.length(),word2.length());
    for (int i=0; i < minLen; ++i){
        word3 += word1[i];
        word3 += word2[i];
    }
    //deal with remaining strings
    return word3 + word1.substr(minLen)+word2.substr(minLen);
    }

int main(){
    string result = mergeAlternately("hello","world");
    cout << result << endl;
    return 0;
}