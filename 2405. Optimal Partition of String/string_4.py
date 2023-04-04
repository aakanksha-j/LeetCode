class Solution:
    def partitionString(self, s: str) -> int:
        partitions = 1 # start with 1 as all characters might be unique
        substring = ''
        for character in s:
            if character in substring:
                partitions += 1
                substring = ''
            substring += character
        return partitions