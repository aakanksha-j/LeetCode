class Solution {
    public int partitionString(String s) {
        int partitions = 1;
        String substring = "";
        for (char character: s.toCharArray()) {
            if (substring.indexOf(character) != -1){
                partitions ++;
                substring = "";
            }
            substring += character;
            //System.out.println(substring);
        }
        return partitions;
    }
}