class Solution:
    """Approach 1: Math - count odd and even elements. cost is the one with
                   lesser no of elements.
       Time complexity: O(n)
       Space complexity: O(1)
       Runtime: 24 ms
       Memory: 14.1 MB"""
    def minCostToMoveChips(self, position):
        odd = even = 0
        for pos in position:
            if pos%2 == 0:
                even += 1
            else:
                odd += 1
        return odd if odd <= even else even


def main():
    position  = [1,2,3]
    s=Solution()
    print(s.minCostToMoveChips(position))
    position  = [2,2,2,3,3]
    print(s.minCostToMoveChips(position))
    position  = [1,1000000000]
    print(s.minCostToMoveChips(position))

if __name__ == '__main__':
    main()
