class Solution {
    public int shortestDistance(String[] wordsDict, String word1, String word2) {
        int minimum = wordsDict.length;
        int w1 = -1, w2 = -1;
        for (int i = 0; i < wordsDict.length; i++){
            String word = wordsDict[i];
            if (word1.equals(word)){
                w1 = i;
            }
            if (word2.equals(word)){
                w2 = i;
            }
            if (w1 != -1 && w2 != -1){
                minimum = Math.min(minimum, Math.abs(w1-w2));
            }
        }
        return minimum;
    }
}