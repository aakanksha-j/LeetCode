class Solution {
public:
    int shortestWordDistance(vector<string>& wordsDict, string word1, string word2) {
        int minimum = size(wordsDict);
        int w1 = -1, w2 = -1;
        for (int i = 0; i < size(wordsDict); i++){
            const string& word = wordsDict[i];
            if (word1 == word){
                w1 = i;
                if (w2 != -1){
                    minimum = min(minimum, w1-w2);
                }
            }
            if (word2 == word){
                w2 = i;
                if (w1 != -1 and word2 != word1){
                    minimum = min(minimum, w2-w1);
                }
            }
        }
        return minimum;
    }
};