class Solution:
    """Approach: Reverse a string using Stack. Implemented a stack using list
                 inside function.
       Time complexity: O(n) because we simply traverse the given string one
                        character at a time and push and pop operations on a
                        stack take O(1) time.
       Space complexity: O(n) as we push all opening brackets onto the stack
                         and in the worst case, we will end up pushing all the
                         brackets onto the stack. e.g. ((((((((((.
       Runtime: 28 ms
       Memory: 14.3 MB
    """

    def isValid(self, s):
        if len(s)%2 != 0:
            return False
        myStack = []
        open_dict = {'{': '}','[': ']','(': ')'}
        for par in s:
            if par in open_dict:
                myStack.append(par)
            elif not myStack or par != open_dict[myStack.pop()]:
                return False
        return True if not myStack else False # if does not contain :

def main():
    p = Solution()
    mystr = "()[]{}"
    print(mystr, ':', p.isValid(mystr))
    mystr = "()"
    print(mystr, ':', p.isValid(mystr))
    mystr = "(]"
    print(mystr, ':', p.isValid(mystr))
    mystr = "([)]"
    print(mystr, ':', p.isValid(mystr))
    mystr = "{[]}"
    print(mystr, ':', p.isValid(mystr))
    mystr = "(("
    print(mystr, ':', p.isValid(mystr)) # wrong answer
    mystr = "){"
    print(mystr, ':', p.isValid(mystr)) # runtime error: pop from empty list

if __name__ == '__main__':
    main()
