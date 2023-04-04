# include <string>

class Solution {
public:
    int partitionString(string s) {
        int partitions = 1;
        unordered_set<char> character_set;
        for (int index = 0; index < s.length(); index++){
            if (character_set.find(s[index]) != character_set.end()){
                partitions += 1;
                character_set.clear();               
            }
            character_set.insert(s[index]);
        }
        return partitions;
    }
};