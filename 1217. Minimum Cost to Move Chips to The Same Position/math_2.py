class Solution:
    """Approach 1: Math - count odd and even elements. cost is the one with
                   lesser no of elements. Use min and LC to make code short.
       Time complexity: O(n)
       Space complexity: O(1)
       Runtime: 32 ms
       Memory: 14 MB"""
    def minCostToMoveChips(self, position):
        odd = sum(x%2 for x in position)
        return min(odd, len(position) - odd)


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
