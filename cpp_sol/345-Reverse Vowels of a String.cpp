class Solution {
public:
    string reverseVowels(string s) {
      int i = 0;
      int j = s.size() - 1;
      while (i < j) {
        while (!isVowel(s[i]) && i < j) ++i;
        while (!isVowel(s[j]) && i < j) --j;                
        swap(s[i++], s[j--]);
      }
      return s;
    }
private:
  bool isVowel(char c) {
    c = tolower(c);
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
  }
};

//ref https://zxi.mytechroad.com/blog/two-pointers/leetcode-345-reverse-vowels-of-a-string/