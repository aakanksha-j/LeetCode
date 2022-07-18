class Solution:
    def simplifyPath(self, path: str) -> str:
        # https://leetcode.com/problems/simplify-path/discuss/1847357/C%2B%2B-oror-Easy-oror-Stack-oror-Simple-oror-Explained-oror-Algorithm

        # while inside while loop
        # using '/' as separator, traverse the string, when word is '.', ''
        # or '/', go to next string and continue in while loop. When word is '..'
        # and stack has an element, pop from the stack. When word is none of the
        # above, add it to stack.

        # time: O(N) - traverse the string once
        # space: O(N) - space for stack

        # this was the only solution without using path.split('/')
        # in this method, we split the string based on delimiter into a list in
        # the form ['word', '', '.', '..'], and then while traversing the list,
        # add to the stack if it is a valid directory name.

        stack = []

        i = 0
        while i < len(path):
            print(path[i], stack)

            if path[i] == '/':
                i += 1
                continue

            else:
                cur = ''
                while i < len(path) and path[i] != '/':
                    cur += path[i]
                    i += 1

                print(cur)
                if cur == '..':
                    if stack:
                        stack.pop()
                elif cur == '.' or cur == '':
                    i += 1
                    continue
                else:
                     stack.append(cur)

        print(stack)

        return '/' + '/'.join(stack)
