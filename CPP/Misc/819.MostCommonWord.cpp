/*
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

Example:
Input: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
 

Note:

1 <= paragraph.length <= 1000.
1 <= banned.length <= 100.
1 <= banned[i].length <= 10.
The answer is unique, and written in lowercase (even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
Different words in paragraph are always separated by a space.
There are no hyphens or hyphenated words.
Words only consist of letters, never apostrophes or other punctuation symbols.
*/

#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <unordered_map>

using namespace std;

int main() {
  string sentence = "The quick brown fox jumped over the lazy dog.";
  int i=0;

  unordered_map<string, int> mp;
  while(i<sentence.size()){
    string s;    
    if(isalpha(sentence[i])){
      while(i<sentence.size() && isalpha(sentence[i])){
        s.push_back(tolower(sentence[i++]));
      }
      mp[s]++;
    }
    else{
      while(i<sentence.size() && !isalpha(sentence[i])){
        i++;
      }
    }
  }

  for(auto elem:mp){
    cout << elem.first << " " << elem.second << endl;
  }
  return 0;
}

  string sentence = "The quick brown fox jumped over the lazy   dog!.";
  istringstream iss(sentence);
  string w;
  while(iss >> w){
    cout << w << endl;
  }