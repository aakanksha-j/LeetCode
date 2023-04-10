#include <stack>
#include <unordered_map>
#include <string>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> hashmap = {{'{','}'}, {'(',')'}, {'[',']'}};
        stack<char> st;
        for (char bracket: s){
            if (hashmap.count(bracket)){
                st.push(bracket);
            }
            else {
                if (st.empty() || bracket != hashmap[st.top()]) {
                    return false;
                }
                st.pop();
            }
        }
        return st.empty();   
    }
};