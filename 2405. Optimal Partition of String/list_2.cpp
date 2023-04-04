# include <vector>
# include <string>

class Solution {
public:
    int partitionString(string s) {
        int partitions = 1;
        vector<int> last_seen_list(26, -1);
        int partition_start = 0;
        for (int index = 0; index < s.length(); index++){
            if (last_seen_list[s[index] - 'a'] >= partition_start){
                partitions += 1;
                partition_start = index;
            }
            last_seen_list[s[index] - 'a'] = index;
        }
        return partitions;
    }
};