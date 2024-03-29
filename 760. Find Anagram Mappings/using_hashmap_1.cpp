#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> anagramMappings(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> nums2_map;
        for (int i = 0; i < nums2.size(); i++) {
            nums2_map[nums2[i]] = i;
        }
        vector<int> output;
        for (int num : nums1) {
            output.push_back(nums2_map[num]);
        }
        return output;
    }
};

int main() {
    Solution s;
    vector<int> nums1 = {2, 4, 6, 8};
    vector<int> nums2 = {8, 2, 6, 4};
    vector<int> output = s.anagramMappings(nums1, nums2);
    for (int num : output) {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}