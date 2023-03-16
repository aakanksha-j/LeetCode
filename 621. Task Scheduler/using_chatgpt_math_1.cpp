class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {  
        /* using chatgpt */

        vector<int> frequencies(26, 0);

        for (char task : tasks) {
            frequencies[task - 'A']++;
        }

        int f_max = *max_element(frequencies.begin(), frequencies.end());
        int n_max = count(frequencies.begin(), frequencies.end(), f_max);

        return max((int)tasks.size(), (f_max - 1) * (n + 1) + n_max);
    }
};