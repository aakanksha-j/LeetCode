/* The knows API is defined for you.
      bool knows(int a, int b); */

class Solution {
public:
    int findCelebrity(int n) {
        int candidate = 0;
        for(int i = 1; i < n; i++){
            if (candidate == i){
                continue;
            }
            if (knows(candidate, i) || !(knows(i, candidate))){
                candidate = i;
            }
        }
        
        for(int j = 0; j < n; j++){
            if (candidate == j){
                continue;
            }
            if (knows(candidate, j) || !(knows(j, candidate))){
                return -1;
            }
        }
        
        return candidate;
    }
};