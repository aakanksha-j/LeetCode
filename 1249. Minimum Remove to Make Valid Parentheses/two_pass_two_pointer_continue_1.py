class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # leetcode solution - shortened two pass string builder

        # approach - Two pass, two lists, 3 pointers, 2 continue
        # 1. first pass - while iterating through the string, keep adding ch to list, take count of open parenthesis, add its count to balance pointer and open_seen,
        # 2. tally balance in first pass to find unmatched '(' closed parenthesis, keep matching it to open ones using balance pointer and append to list otherwise continue
        # 3. second pass - Traverse the first pass list now and check for unmatched '(' using open_balance pointer - (open seen - balance).
        # Append empty string if pointer < 0. Otherwise keep appending the characters from first pass list to the second list
        # 4. Use join function on second list to get output string.

        # time - O(n) we process each ch once or twice for '('
        # space - O(n) for two lists


        first_pass_chars = [] # to store unmatched open parenthesis
        open_seen = balance = 0 # to match ')' to '('

        for ch in s:
            if ch == '(':
                balance += 1
                open_seen += 1
            elif ch == ')':
                if balance == 0:
                    continue
                balance -= 1
            first_pass_chars.append(ch)

        res = [] # to store the output string in list form
        open_balance = open_seen - balance
        for ch in first_pass_chars: # make unmatched '(' as empty strings
            if ch == '(':
                open_balance -= 1
                if open_balance < 0:
                    res.append('')
                    continue
            res.append(ch)

        return ''.join(res)


        
