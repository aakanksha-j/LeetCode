class Solution:
    """Approach 1: Read J and build jewels hash set.
                   Read S and count jewels.
       Time complexity: O(len(jewel) + len(stone)). creating J set and searching S.
       Space complexity: O(J) to build jewels hash set.
       Runtime: 28 ms
       Memory: 14.4 MB
    """
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)
        # print(jewels_set)
        return sum(s in jewels_set for s in stones)


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
