import java.util.Arrays;
    
    
class Solution {
    public int partitionString(String s) {
        int partitions = 1;
        int[] last_seen_list = new int[26];
        Arrays.fill(last_seen_list, -1);
        int partition_start = 0;
        for (int index = 0; index < s.length(); index++) {
            if (last_seen_list[s.charAt(index)- 'a'] >= partition_start) {
                partitions += 1;
                partition_start = index;
            }
            last_seen_list[s.charAt(index) - 'a'] = index;            
        }
        return partitions;
    }
}