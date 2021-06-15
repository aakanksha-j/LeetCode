"""You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.

Example 1:

Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.

Example 2:
Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91

Constraints:

1 <= boxTypes.length <= 1000
1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
1 <= truckSize <= 10^6"""

class Solution:
    def maximumUnits(self, boxTypes, truckSize: int) -> int:
        # sort array in reverse order based on # of units in each box
        boxTypes.sort(key = lambda boxTypes: boxTypes[1], reverse = True)
        print(boxTypes)
        # boxTypes.sort(key=lambda x: -x[1])
        # https://leetcode.com/problems/maximum-units-on-a-truck/discuss/999125/JavaPython-3-Sort-reversely-by-the-units-then-apply-greedy-algorithm.

        # run loop till 0 truck size is reached
        max_units = 0
        curr_size = truckSize
        for n_boxes, n_units in boxTypes:
            if n_boxes <= curr_size:
                max_units += n_boxes * n_units
                curr_size -= n_boxes
            else:
                max_units += curr_size * n_units
                return max_units
        return max_units

def main():
    boxTypes = [[5,10],[2,5],[4,7],[3,9]]
    truckSize = 10
    s=Solution()
    print(s.maximumUnits(boxTypes, truckSize))
    boxTypes = [[1,3],[2,2],[3,1]]
    truckSize = 4
    print(s.maximumUnits(boxTypes, truckSize))
    boxTypes = [[6, 7], [6,8], [8, 9], [9,10]]
    truckSize = 78
    print(s.maximumUnits(boxTypes, truckSize))

if __name__ == '__main__':
    main()

"""time and space complexity - O(n) using timsort"""
