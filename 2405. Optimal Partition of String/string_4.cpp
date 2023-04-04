# include <string>

class Solution {
public:
    int partitionString(string s) {
        int partitions = 1;
        string substring = "";
        for (char character: s){
            if (substring.find(character) != string::npos){
                partitions++;
                substring = "";
            }
            substring += character;
            //cout << substring << endl;
        }
        return partitions;
    }
};