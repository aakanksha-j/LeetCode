# include <string>

class Solution {
public:
    int partitionString(string s) {
        int partitions = 1;
        int flag = 0; // one int variable instead of vector last_seen and partition_start
        for (int index = 0; index < s.length(); index++){
            int val = s[index] - 'a';
            if (flag & (1 << val)){
                partitions += 1;
                flag = 0;
            }
            flag |= 1 << val;
            //cout << flag << endl;
        }
        return partitions;
    }
};