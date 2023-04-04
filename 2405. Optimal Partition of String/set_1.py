class Solution:
    def partitionString(self, s: str) -> int:
        answer = 1 # start with 1 as all characters might be unique
        character_set = set()
        for index in range(len(s)):
            if s[index] in character_set:
                answer += 1
                character_set = set()
            character_set.add(s[index])
        return answer
    
# time O(n)
# space O(26)