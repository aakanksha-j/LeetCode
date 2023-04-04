import java.io;

class Solution {
    public int partitionString(String s) {
        int partitions = 1;
        int flag = 0; // one int variable instead of an array       
        for (int index = 0; index < s.length(); index++) {
            int val = s.charAt(index) - 'a';
            if ((flag & (1 << val)) != 0) {
                partitions += 1;
                flag = 0;
            }
            flag |= 1 << val;        
            //System.out.println(flag);
        }
        return partitions;
    }
}