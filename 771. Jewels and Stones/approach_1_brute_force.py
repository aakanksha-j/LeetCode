class Solution:
    """Approach 1: Linear scan to check for each stone whether it matches any of
                   the jewels.
       Time complexity: O(len(jewel) * len(stone))
       Space complexity: O(1)
       Runtime: 32 ms
       Memory: 14.3 MB
    """
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """count = 0
        for s_ch in stones:
            if s_ch in jewels:
                count += 1
        return count"""
        return sum(s in jewels for s in stones)

def main():
    jewels = "aA"
    stones = "aAAbbbb"
    s=Solution()
    print(s.numJewelsInStones(jewels, stones))
    jewels = "z"
    stones = "ZZ"
    print(s.numJewelsInStones(jewels, stones))
    jewels = "z"
    stones = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
    print(s.numJewelsInStones(jewels, stones))

if __name__ == '__main__':
    main()
