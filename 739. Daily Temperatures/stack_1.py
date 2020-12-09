class Solution:
    """Approach 1: Use a stack to maintain all higher temperatures by traversing
                   backwards. Pop element whenever temperature is less than
                   current one in stack of future ones using while loop. If
                   stack has any element even after popping using while loop
                   then that temp in stack must have been closest temp more than
                   current one so assign the difference between position of that
                   temp and current one to the list of output for current
                   position.                 
       Time complexity: O(n) represents for loop for length of T
       Space complexity: O(W) to store list of strictly increasing temperatures
                         in stack
       Runtime: 500 ms
       Memory: 18.9 MB
    """
    def dailyTemperatures(self, T):

        # preliminary checks
        if len(T) > 30000: return 'Invalid list length.'
        for temp in T:
            if temp < 30 or temp > 100:
                return 'Invalid temperature value.'

        # initialize variables
        ans = [0] * len(T)
        warmer_stack= [len(T) - 1]

        for i in range(len(T) - 2, -1, -1):
            print('i:', i, 'T[i]:', T[i])
            print(warmer_stack)
            while warmer_stack and T[i] >= T[warmer_stack[-1]]:
                # no future temp will be strictly larger than T[i]
                warmer_stack.pop()
            if warmer_stack:
                ans[i] = warmer_stack[-1] - i
            warmer_stack.append(i)
        return ans

def main():
    numbers = [73, 74, 75, 71, 69, 72, 76, 73]
    s=Solution()
    print(s.dailyTemperatures(numbers))
    numbers =[71, 69, 70, 70, 70, 70]
    print(s.dailyTemperatures(numbers))
    # got time limit exceeded for this testcase
    numbers  =[47,34,47,34,47,47,34,34,47,47,34,47,47,47,47,34,47,34,34,47,34,34,34,47,34,47,34,47,34,47,34,34,34,34,34,47,34,34,47,47,47,47,34,34,47,47,34,47,47,34,47,47,47,34,47,34,34,34,34,47,47,34,34,34,47,47,34,34,34,47,34,34,34,34,47,34,34,34,34,47,47,47,34,47,34,34,47,47,34,47,34,34,47,34,34,34,47,34,34,47,34,47,34,47,47,47,34,47,34,47,47,34,47,47,47,47,47,47,47,34,47,47,47,47,34,34,34,34,47,34,34,34,34,34,47,34,47,47,47,47,34,34,47,47,34,47,34,47,47,47,34,47,34,34,34,47,47,47,34,34,34,34,34,47,47,47,47,34,47,47,34,47,34,34,47,34,47,34,34,34,47,34,34,34,47,47,47,47,47,47,47,47,34,47,47,47,47,34,34,34,47,34,34,34,34,47,47,47,34,34,34,34,47,34,47,34,34,47,47,47,34,34,47,34,47,34,34,47,47,34,34,47,34,47,47,47,47,34,47,34,47,34,47,34,34,34,47,47,47,34,34,47,34,47,34,47,47,34,34,47,34,34,47,34,34,47,47,34,34,47,47,47,34,34,47,47,47,34,47,47,47,47,47,34,34,34,34,34,34,34,47,47,34,47,34,47,47,47,47,47,47,47,47,47,47,34,47,47,47,34,47,34,34,34,47,47,47,47,34,47,34,47,34,47,47,34,34,34,47,34,34,47,34,47,34,47,34,34,34,34,47,47,34,47,47,47,34,47,34,34,47,34,47,34,47,34,47,34,47,34,47,47,34,34,47,34,47,47,47,47,47,34,34,34,47,34,47,34,34,47,47,47,34,47,47,47,47,34,34,47,47,34,34,34,47,47,47,34,47,47,47,34,47,34,34,47,47,34,47,34,34,47,34,34,34,34,47,47,47,34,47,47,34,47,47,34,34,34,34,47,34,34,47,34,47,47,47,34,47,34,34,47,34,47,34,34,34,34,34,34,47,47,47,47,47,47,47,34,34,34,47,34,34,47,47,47,34,47,34,47,34,47,34,47,47,47,34,34,34,34,34,34,34,34,47,47,47,34,47,34,34,34,47,34,47,47,34,47,47,47,34,34,34,34,34,47,34,47,34,34,47,34,47,47,34,34,34,34,47,47,34,34,47,47,34,34,34,34,34,34,34,47,34,34,47,34,34,47,34,34,47,34,34,34,47,47,34,34,47,47,47,34,34,47,47,47,34,47,47,47,47,47,47,47,34,47,47,47,34,47,47,34,47,34,34,47,34,34,34,34,34,34,47,47,47,34,47,47,34,47,34,34,47,34,34,34,47,47,34,47,47,34,34,34,47,47,47,47,34,47,34,34,47,47,47,47,47,34,47,34,34,34,47,47,47,34,34,47,47,34,34,34,34,34,47,34,47,34,47,34,47,47,47,47,47,34,47,34,34,34,34,34,47,34,47,47,34,34,47,34,47,34,47,34,47,34,47,34,47,47,34,47,47,47,47,34,34,47,34,34,34,34,47,34,34,47,34,34,34,34,34,47,34,47,34,47,34,47,47,47,34,47,34,34,47,47,34,34,34,34,34,34,47,47,47,47,47,47,34,34,34,34,34,47,47,34,47,47,34,47,34,34,47,34,34,47,47,47,34,47,34,47,47,47,47,34,47,47,34,34,34,34,34,34,47,47,47,47,47,47,47,47,47,34,34,34,47,34,34,47,34,47,34,47,34,47,34,47,47,47,34,34,34,34,47,34,47,47,47,34,34,34,47,47,34,34,47,47,47,34,47,34,47,47,47,47,34,34,34,34,47,34,47,47,47,34,47,47,34,47,34,47,47,47,34,47,34,47,34,47,47,47,47,47,34,34,34,47,47,47,34,47,34,34,34,34,34,34,34,47,47,47,47,47,47,34,47,47,47,34,34,34,47,47,47,47,47,34,34,47,47,34,34,34,34,47,34,34,34,47,34,47,34,47,47,47,47,47,47,34,47,34,47,34,47,34,34,34,34,34,34,47,47,47,34,34,34,34,34,47,34,34,34,47,47,47,34,47,34,47,34,34,47,47,34,34,47,34,47,47,34,47,34,47,34,47,47,34,34,47,47,34,34,34,47,34,34,47,47,34,47,47,34,34,34,47,34,34,34,47,34,34,34,47,47,34,47,34,47,34,47,34,34,34,47,34,34,47,34,47,34,47,47,47,47,47,47,47,34,47,34,34,47,47,34,34,47,34,34,47,47,47,34,47,34,34,47,47,34,34,34,34,34,47,47,34,47,47,34,47,34,34,34,47,34,34,34,47,47,34,34,34,34,34,47,47,47,34,47,47,47,47,34,47,47,47,47,47,34,34,47,47,47,47,34,34,34,47,34,47,47,34,47,47,34,34,47,47,47,47,47,47,34,47,47,34,34,34,47,47,47,47,34,47,47,47,34,47,47,34,34,34,47,34,34,34,47,34,47,34,47,34,47,47,47,47,34,47,34,47,34,47,34,34,47,34,34,47,34,47,47,47,47,34,47,34,47,34,34,34,34,47,34,34,34,47,34,47,47,34,47,34,47,34,47,47,47,47,47,47,34,34,47,47,34,34,47,47,47,47,47,34,47,34,34,47,47,34,34,47,47,47,34,47,34,47,34,47,47,34,47,34,34,47,34,34,47,47,47,34,34,47,47,34,47,47,47,34,47,34,34,47,34,34,47,47,34,34,47,47,34,34,47,47,34,47,34,34,47,34,34,47,47,47,47,47,34,47,47,34,34,34,34,34,47,47,34,47,47,34,47,47,34,47,47,47,47,34,34,34,34,34,34,34,47,34,47,47,34,34,34,47,34,34,47,34,47,47,34,34,47,47,34,47,47,47,47,47,47,47,47,34,34,47,47,47,34,34,34,47,47,47,47,47,47,34,47,47,47,34,34,34,34,34,34,47,47,34,47,34,47,47,47,34,34,47,34,34,34,34,47,34,34,47,34,47,47,34,34,47,34,34,34,47,34,47,47,34,47,47,34,47,47,34,34,47,47,34,34,34,47,47,47,47,47,34,34,34,34,34,34,47,47,34,34,34,34,34,47,34,47,34,47,47,34,47,47,47,47,34,47,34,47,47,34,34,47,47,34,34,47,47,47,47,34,47,47,47,34,47,47,34,34,47,47,34,34,34,47,47,34,34,47,34,34,34,47,47,34,34,34,47,47,34,47,47,47,47,47,47,34,47,47,47,47,34,34,47,47,47,34,34,47,47,47,34,34,47,47,47,47,34,34,47,47,34,47,47,34,47,47,47,47,47,47,47,47,47,47,47,47,34,34,47,34,47,47,34,34,47,34,34,34,34,34,47,34,47,47,47,34,47,47,34,34,34,47,47,47,47,47,34,47,47,47,34,47,34,34,34,47,34,34,34,47,47,47,47,34,34,34,34,34,47,47,34,47,47,34,47,47,47,34,34,34,34,47,34,47,47,47,47,47,47,47,34,34,47,47,47,34,34,34,34,34,34,34,47,34,47,34,34,47,34,34,34,47,34,34,47,47,34,47,34,47,47,34,34,34,34,47,47,34,34,34,47,47,34,47,47,34,34,47,34,47,34,34,34,47,34,34,34,34,47,47,34,47,47,34,34,47,34,34,34,47,34,34,34,34,34,47,34,47,34,34,34,34,34,34,47,34,34,47,34,47,34,34,34,47,47,47,34,34,47,47,47,34,47,34,47,34,34,34,34,34,34,47,34,34,34,47,34,34,47,34,47,34,47,47,47,34,34,47,34,47,47,47,47,34,47,47,34,34,47,34,34,34,34,34,34,34,47,34,47,47,47,34,34,47,34,34,34,34,34,34,34,34,47,34,47,34,34,47,34,47,47,34,34,47,47,47,47,34,34,34,34,34,47,34,47,34,47,34,47,47,34,34,47,47,47,34,47,34,34,47,34,47,47,47,34,47,34,34,34,34,47,34,34,34,34,47,34,34,47,47,47,34,34,47,47,47,47,47,34,34,34,47,47,47,34,47,47,34,47,34,34,34,34,47,47,47,47,34,47,47,34,34,47,34,47,47,34,47,47,34,34,47,47,47,47,34,47,47,34,34,34,34,47,34,47,47,34,34,47,47,34,47,34,34,47,34,47,34,47,47,47,34,47,34,47,47,47,34,34,47,34,47,34,34,34,47,47,34,47,47,34,34,47,47,47,47,47,34,47,47,47,47,47,47,47,34,47,34,34,34,34,34,34,47,47,34,47,34,47,47,47,34,47,47,34,47,47,47,47,47,34,47,47,47,34,34,34,34,47,47,34,47,47,34,47,34,34,47,34,47,47,34,47,34,34,34,47,47,47,47,34,34,34,34,34,34,34,34,34,34,47,34,47,47,47,34,34,47,47,47,47,47,47,47,34,47,34,47,34,34,34,34,34,47,47,47,47,47,47,34,47,47,34,47,47,34,34,34,47,47,34,34,47,34,34,34,47,47,34,34,47,47,34,34,34,47,34,47,34,47,34,34,47,47,47,47,47,47,34,47,47,47,47,47,47,34,47,34,34,47,34,34,34,34,47,47,47,34,47,34,34,47,47,47,47,34,47,34,34,47,47,34,47,47,34,47,34,47,34,47,47,34,34,34,34,34,47,47,34,47,34,47,34,34,47,34,34,47,34,34,47,47,47,47,34,47,34,47,47,47,34,34,47,34,47,34,34,34,47,47,34,34,34,34,34,34,47,47,47,47,47,47,47,34,47,47,47,34,34,47,34,34,47,47,34,47,47,34,47,47,34,34,34,47,34,47,34,34,47,47,34,47,47,47,34,34,47,34,34,34,47,47,34,34,34,34,34,47,34,47,47,34,34,47,34,47,47,34,47,47,34,47,47,34,47,47,47,34,34,47,47,34,34,34,34,47,47,47,34,34,47,47,34,34,47,47,34,47,34,47,34,34,34,34,34,34,34,34,34,47,47,47,47,34,34,34,47,47,47,47,47,34,47,47,34,47,34,47,47,34,47,34,34,47,34,34,47,47,47,47,47,34,34,34,47,34,47,47,47,47,47,47,34,34,47,34,47,47,34,47,47,34,34,34,47,47,47,34,47,47,47,47,47,34,47,34,47,34,47,34,34,34,47,47,47,34,47,47,47,34,47,47,47,47,47,47,34,47,47,47,47,34,47,34,34,47,47,34,47,34,47,47,34,47,34,34,34,47,47,34,47,34,47,34,47,34,34,47,34,47,47,47,34,47,34,47,47,34,34,47,34,47,34,34,34,34,34,34,47,34,34,34,34,34,34,34,47,47,47,47,47,47,34,47,47,47,34,47,34,47,47,34,34,34,34,34,47,47,47,47,47,47,34,47,47,47,47,34,47,47,47,47,34,34,47,47,47,47,34,47,34,47,47,47,34,47,34,47,34,47,34,47,47,34,47,47,34,34,47,47,34,47,47,47,47,47,34,47,47,47,34,47,47,47,47,47,47,47,47,47,34,34,47,34,34,34,47,47,34,47,47,47,34,34,47,34,47,47,34,34,34,47,47,34,47,47,47,47,47,34,34,34,34,47,47,34,47,34,34,34,34,34,47,47,34,47,47,34,47,34,34,47,34,34,34,47,47,34,34,34,47,34,34,34,47,34,47,34,34,47,47,34,34,34,47,34,34,47,34,47,34,34,47,47,47,47,34,47,34,34,47,34,34,34,47,47,34,47,34,47,47,34,47,47,47,47,47,34,34,47,34,34,47,47,47,47,47,47,47,47,34,47,34,47,47,34,34,34,34,34,47,47,47,47,34,47,34,47,47,34,47,34,47,34,47,34,47,34,34,47,34,47,47,34,47,34,47,47,34,34,47,34,34,47,34,47,47,47,47,34,34,47,34,34,47,34,47,47,47,47,34,47,47,34,34,47,47,47,47,34,47,34,47,34,47,47,34,47,34,47,34,47,47,34,34,47,47,47,47,34,34,34,47,47,47,47,34,34,47,34,47,47,47,34,47,47,34,47,34,47,47,34,34,34,47,34,47,47,34,47,47,34,47,34,34,34,47,47,34,34,47,47,47,34,47,47,34,47,47,47,34,34,47,34,47,47,47,47,34,47,34,34,34,47,47,47,47,34,47,47,47,34,34,47,34,47,34,47,34,47,47,34,34,34,34,34,34,47,47,34,34,34,47,34,47,34,34,34,47,34,47,34,34,34,47,34,34,47,47,47,34,34,34,34,34,34,34,47,34,47,34,34,47,34,47,47,34,47,47,34,47,47,34,47,34,34,34,47,47,34,47,34,47,34,47,47,34,34,47,47,34,34,47,47,34,34,34,47,34,47,47,34,47,34,34,34,47,47,47,34,34,34,34,34,34,47,34,47,34,34,34,47,47,47,34,34,47,34,34,47,47,47,47,34,34,47,47,47,47,47,34,34,34,34,47,34,34,47,47,47,34,47,34,34,34,34,47,34,34,34,47,47,34,34,47,47,47,34,34,47,34,34,47,47,47,47,47,34,34,34,47,47,47,34,47,34,34,34,47,34,34,34,34,47,47,47,34,34,47,47,47,47,34,47,34,47,34,34,34,47,47,47,47,47,47,34,34,47,47,34,34,34,47,34,47,34,34,34,34,34,47,34,47,47,34,47,47,34,34,34,47,34,47,47,47,47,47,34,47,47,34,34,47,34,47,47,34,47,34,34,47,34,47,34,47,34,34,47,47,47,47,47,47,34,34,34,34,47,34,34,47,34,34,47,34,47,47,34,34,47,47,47,34,47,34,34,34,47,47,34,34,47,47,34,47,47,34,34,34,34,34,34,34,47,34,34,47,47,47,34,34,47,47,47,34,34,47,34,34,34,34,34,34,34,34,47,34,34,34,47,47,34,47,34,34,47,34,34,34,47,34,34,47,34,34,34,47,34,34,47,34,47,34,47,34,34,47,34,47,47,34,47,34,34,47,34,47,47,47,34,34,47,47,47,47,34,34,34,34,34,47,47,47,34,47,34,34,34,47,47,34,34,47,34,47,47,47,47,47,47,47,34,34,34,47,34,47,34,47,34,34,47,47,34,47,47,47,47,47,47,47,47,34,34,34,34,47,47,47,47,47,34,34,47,34,34,34,47,34,47,47,34,34,34,34,34,34,34,34,34,47,34,34,47,47,47,34,34,34,47,47,47,47,47,47,47,47,47,47,34,47,47,47,47,34,47,34,34,34,47,47,34,47,47,47,47,34,47,34,34,34,47,47,47,47,34,47,34,47,34,34,47,47,34,34,34,34,47,47,47,47,47,34,47,34,34,34,34,47,47,34,47,34,34,34,47,47,34,34,47,47,47,47,47,34,47,47,47,34,47,47,47,47,47,34,34,47,34,34,34,34,47,47,47,34,47,47,34,47,47,47,34,47,47,47,47,47,34,47,47,47,47,34,47,47,47,47,47,34,47,34,47,47,34,47,34,34,47,47,34,47,47,47,47,47,34,34,47,34,47,47,34,34,47,34,47,47,47,34,34,34,34,34,34,47,34,34,47,34,47,47,47,47,34,34,34,34,47,34,47,34,47,34,34,34,34,34,47,34,34,34,47,47,34,34,47,34,34,47,34,34,47,47,47,34,47,47,47,34,47,34,34,47,47,47,34,47,34,47,34,34,47,47,34,47,34,47,47,34,34,34,47,34,47,47,47,34,47,34,34,34,47,34,47,47,34,47,47,47,34,47,34,47,47,34,34,47,34,34,34,34,47,47,34,34,34,34,34,34,47,34,34,47,34,47,47,47,47,34,34,47,34,47,34,34,34,34,34,47,34,47,47,34,47,47,34,47,34,47,34,34,47,34,47,47,34,34,34,34,34,34,34,47,47,47,34,34,34,34,34,47,34,34,47,47,34,34,34,47,47,34,34,47,47,34,34,47,47,34,47,47,47,47,47,47,47,34,47,34,34,47,34,34,34,34,47,34,47,34,47,34,34,34,34,47,34,47,47,34,34,47,47,34,34,34,34,47,47,47,47,47,47,34,34,47,34,47,47,34,47,34,34,34,47,47,47,47,47,34,34,34,47,47,47,47,34,34,34,34,47,47,47,34,34,34,34,34,47,34,34,47,47,47,47,34,47,34,47,47,47,34,34,47,34,47,47,34,47,47,34,34,47,47,47,47,47,34,34,34,34,47,34,47,47,47,47,47,34,34,47,47,34,47,47,34,34,34,34,47,47,34,47,34,47,34,47,34,34,47,34,47,34,47,47,47,47,47,34,34,34,47,47,34,34,34,47,34,47,34,34,34,34,34,34,34,34,47,34,34,34,47,34,47,47,34,47,34,47,34,47,47,47,34,34,47,34,47,47,34,47,47,34,47,34,47,34,34,47,34,47,34,47,47,47,34,34,47,47,47,47,47,47,47,34,34,34,47,47,34,47,34,47,34,34,34,47,34,47,34,47,34,47,47,47,34,47,47,47,34,47,47,47,47,34,47,47,34,34,47,47,47,34,47,47,47,34,47,47,34,34,47,47,47,47,34,47,34,47,34,47,34,34,34,47,47,34,47,34,34,34,34,34,47,34,34,34,47,47,47,47,47,34,47,34,47,34,47,34,47,34,47,34,47,34,47,34,47,34,47,34,34,34,34,47,34,34,47,47,47,47,47,47,34,34,47,47,34,34,34,34,34,34,47,47,47,47,34,47,34,47,47,47,34,34,47,47,34,34,34,34,34,34,47,34,34,47,34,47,34,47,34,34,47,34,34,34,47,34,47,34,34,47,47,34,47,47,47,34,47,34,34,34,47,34,34,34,34,47,47,34,34,34,34,34,47,34,47,34,47,34,47,34,47,34,34,47,34,47,47,34,47,47,47,34,47,34,47,47,47,34,47,47,47,47,34,47,47,47,47,34,47,47,47,34,47,47,47,34,47,34,34,47,47,47,47,47,34,34,34,47,34,34,47,47,34,34,34,47,47,47,34,34,34,34,34,47,34,47,34,34,47,34,47,47,47,34,34,47,34,34,34,34,34,34,47,47,47,34,34,47,34,47,47,47,47,34,47,34,34,34,47,34,47,34,34,47,47,47,47,47,47,47,34,34,47,47,47,47,47,47,47,34,34,34,47,47,47,47,47,34,34,34,34,34,34,47,34,34,47,34,34,47,47,34,47,34,47,34,47,47,47,34,34,34,34,34,34,34,47,34,47,34,47,47,34,34,34,34,47,34,47,47,34,34,47,34,47,34,34,47,47,47,34,47,47,47,34,34,47,34,47,34,47,34,34,47,34,47,47,47,47,47,34,34,47,47,47,47,47,47,34,34,47,47,34,34,34,34,47,47,47,34,34,34,47,34,34,47,47,47,47,47,34,47,34,47,47,34,47,47,34,47,47,34,34,47,47,34,47,34,47,47,34,34,34,47,34,47,34,34,47,47,34,34,34,34,34,34,34,47,34,47,47,47,34,34,47,34,47,47,47,34,34,47,34,47,47,34,34,34,34,47,47,47,34,34,47,34,34,47,47,47,47,47,47,34,47,34,47,47,34,47,34,34,34,34,47,34,47,34,34,34,47,34,47,47,47,47,34,34,47,34,47,34,47,47,47,34,34,34,47,47,34,34,34,34,47,34,47,47,47,34,47,34,34,47,34,47,47,47,47,47,47,47,47,47,34,47,47,34,47,34,47,47,47,47,47,47,47,34,34,47,47,34,34,34,34,34,47,34,34,34,47,47,47,34,34,47,34,47,47,34,34,47,34,34,47,47,47,47,47,34,34,47,47,34,47,34,47,34,34,47,47,34,34,47,47,34,34,47,47,34,47,47,47,47,34,34,34,34,34,34,34,34,47,47,34,34,47,47,47,47,47,34,47,47,34,47,34,47,34,34,34,47,34,34,47,34,34,34,34,34,47,47,47,34,47,34,47,34,34,34,34,47,47,34,47,34,34,47,34,34,34,34,34,34,34,47,47,34,34,47,34,47,34,47,47,34,47,34,47,47,47,34,47,34,47,34,34,47,47,47,47,47,34,34,34,34,47,34,34,47,34,47,34,34,34,34,34,47,47,34,47,47,47,47,47,34,34,34,47,47,34,47,47,47,34,47,47,34,47,34,47,34,34,34,34,34,47,47,34,34,47,34,47,34,34,34,34,34,47,47,47,47,47,47,47,34,47,47,47,47,34,34,34,47,47,34,34,34,47,47,47,34,34,34,47,47,34,34,47,34,34,47,34,47,34,34,34,34,34,34,47,34,47,34,34,34,34,47,47,34,47,34,47,34,47,34,47,47,34,47,47,47,47,34,47,34,34,34,47,47,47,47,47,34,47,34,34,34,34,34,47,34,34,34,47,34,47,47,34,47,34,47,47,47,47,34,34,47,34,34,34,47,34,34,34,34,34,34,47,34,47,47,47,47,47,47,34,47,47,34,34,47,47,34,47,47,47,34,34,34,34,34,47,47,34,47,34,34,34,47,34,34,34,34,47,47,34,47,47,47,34,47,47,47,47,34,34,34,47,34,47,47,47,34,47,47,34,47,34,47,34,34,47,47,47,34,34,47,47,47,34,47,47,34,34,47,47,47,34,34,34,34,47,47,47,34,47,47,34,34,47,47,47,47,34,34,34,47,47,34,34,34,47,47,34,47,34,34,47,47,47,34,34,34,34,34,34,34,34,34,34,34,34,34,34,47,34,47,34,47,34,47,34,47,47,47,34,47,34,47,34,47,34,34,34,47,47,34,47,34,34,47,47,47,34,47,34,47,47,47,34,34,47,34,34,34,34,47,47,47,47,34,47,34,47,47,47,47,34,34,47,47,34,47,34,47,47,34,47,34,34,34,47,34,34,47,47,47,47,47,47,34,34,34,34,47,34,47,47,47,47,47,34,34,34,47,34,47,34,47,47,34,34,47,47,34,47,34,47,34,34,34,34,47,34,34,34,47,34,34,34,47,34,34,34,47,47,47,47,47,34,34,34,34,47,34,34,47,47,47,34,34,47,34,34,47,47,34,34,47,47,47,47,47,34,47,47,34,47,34,47,34,47,47,47,34,34,34,34,47,34,34,47,34,47,47,47,47,34,47,34,47,34,34,34,47,47,34,34,47,47,47,34,34,47,34,47,34,47,34,47,34,47,47,47,34,34,47,47,47,47,34,47,47,47,47,34,47,47,47,34,34,34,47,47,34,47,47,34,34,47,34,34,47,47,47,47,47,47,47,47,47,34,34,34,47,47,34,34,47,47,47,47,47,47,47,47,47,34,34,34,47,34,34,34,47,34,47,47,47,47,47,34,34,34,34,34,34,34,34,47,47,47,47,34,47,34,47,47,47,34,47,34,34,34,47,47,47,47,34,47,47,34,47,47,34,34,34,47,34,34,34,47,34,34,34,34,47,47,47,47,34,34,47,47,47,47,34,47,47,34,34,34,47,47,34,34,34,47,47,47,34,47,47,34,47,34,47,47,47,34,34,47,34,34,34,34,47,47,47,47,34,34,47,34,47,47,47,47,34,47,34,34,47,47,47,34,47,34,34,47,34,34,47,34,34,47,34,47,34,47,34,34,47,47,47,34,47,47,34,47,34,47,34,47,34,34,34,47,47,47,47,47,47,47,34,47,34,34,34,47,34,47,47,34,47,34,47,34,34,47,34,47,34,47,34,47,34,47,47,34,34,34,47,47,34,47,47,47,47,34,34,47,47,34,34,34,34,34,47,34,47,34,34,47,47,34,47,47,34,34,47,34,34,34,34,47,47,34,34,47,34,47,34,47,34,34,34,34,34,47,34,47,47,47,47,47,47,47,34,47,34,47,47,47,34,34,34,34,47,34,47,47,34,47,34,34,34,47,34,34,47,34,47,47,47,47,34,34,34,47,34,34,34,47,47,34,47,34,34,47,34,47,34,34,47,34,34,34,47,34,47,34,47,34,47,47,34,47,47,34,47,47,34,47,34,47,34,34,34,34,47,47,47,34,34,34,47,47,47,47,34,34,34,47,47,34,34,34,34,34,34,34,34,47,34,47,47,47,47,47,34,34,34,34,47,47,47,34,47,47,47,47,47,47,47,34,34,47,34,47,34,47,47,34,47,34,47,47,47,47,34,34,34,34,47,34,34,34,34,34,47,47,34,47,34,47,34,34,34,47,34,34,47,47,34,47,47,34,47,47,34,34,34,47,34,34,47,47,47,34,34,34,47,34,34,47,47,47,34,34,34,34,47,34,47,34,47,34,47,47,34,47,34,34,34,34,47,47,47,47,47,34,47,47,47,47,34,34,34,47,47,47,34,47,47,34,47,47,34,47,47,47,34,34,47,34,47,34,47,34,47,47,34,47,34,47,47,34,34,34,34,34,47,47,47,47,47,34,47,47,34,34,47,47,34,34,34,47,47,47,34,47,34,34,47,34,47,47,47,47,47,34,47,34,47,34,47,34,47,34,34,34,47,34,47,34,47,34,34,47,47,47,34,34,34,47,34,34,34,47,47,47,47,34,47,47,34,34,47,34,34,34,47,34,34,47,34,34,47,47,47,47,34,34,34,34,47,47,34,47,34,47,34,34,34,47,47,34,34,47,34,47,47,34,34,47,34,34,34,34,34,47,34,47,47,47,34,47,47,47,34,47,47,47,47,34,47,34,47,47,47,34,34,34,47,47,34,34,34,47,47,34,47,34,34,34,47,34,34,47,34,47,47,47,47,34,47,34,34,47,34,34,47,47,34,47,34,34,47,47,47,34,34,47,47,34,47,34,34,34,34,34,34,47,47,47,47,34,34,47,47,47,47,34,34,34,34,34,47,47,47,47,47,34,47,34,47,47,34,34,47,34,34,47,47,47,34,47,34,47,34,34,47,47,34,47,34,47,47,47,47,47,47,34,34,47,47,47,34,47,34,34,34,34,47,47,34,34,47,34,34,34,34,47,34,34,47,34,47,34,34,47,34,34,47,47,34,34,47,47,47,47,47,34,34,34,34,47,34,47,34,34,47,34,34,34,34,47,47,47,47,47,47,34,34,34,47,34,34,47,34,47,47,34,47,34,47,47,47,47,34,47,34,47,47,34,47,34,34,47,34,34,34,47,34,47,34,47,47,34,34,47,34,47,47,47,47,34,34,34,47,47,34,47,34,34,47,47,47,47,34,34,47,34,34,34,47,47,47,34,47,47,47,34,34,34,34,34,34,47,47,47,34,47,47,47,34,34,34,47,34,34,34,47,47,34,34,47,47,47,47,47,47,47,34,34,47,34,34,47,34,34,47,47,34,47,47,47,47,34,34,47,34,47,47,34,34,47,34,47,34,34,34,34,47,34,47,34,47,47,47,34,47,34,34,34,47,47,34,47,47,47,34,34,47,47,34,47,34,47,47,34,47,34,47,34,34,34,47,47,34,47,47,34,34,47,34,47,47,47,47,34,34,47,47,34,47,47,34,47,34,34,34,47,47,34,47,34,34,34,47,47,34,34,34,34,34,34,34,34,47,47,47,34,34,34,34,47,47,47,34,47,47,34,34,47,34,34,34,47,34,47,34,47,47,47,34,34,47,47,47,34,47,47,47,34,34,47,34,47,47,47,47,34,34,34,47,34,34,47,47,34,34,47,34,47,34,34,34,34,47,47,34,34,34,34,34,34,47,34,47,47,47,34,47,34,47,47,34,34,34,34,47,34,34,47,47,34,34,47,34,47,34,47,47,34,47,47,47,34,47,34,47,34,47,34,34,47,47,34,34,34,34,47,34,47,47,34,47,34,47,34,34,34,47,47,47,34,47,34,34,47,47,34,47,47,47,47,47,47,47,47,34,47,34,47,34,34,34,34,47,47,34,47,47,47,47,47,47,47,47,34,34,34,34,34,47,47,34,47,47,47,47,34,34,47,47,34,34,34,34,47,34,34,34,47,47,34,34,34,47,34,34,47,47,34,34,47,34,47,47,47,47,47,34,34,47,47,47,47,47,47,34,47,47,47,34,47,47,34,34,47,47,34,34,34,34,47,47,34,47,47,34,34,34,47,47,47,34,47,47,34,34,47,34,47,47,34,34,47,47,47,47,47,47,47,34,34,34,34,34,34,34,34,47,34,47,47,34,47,34,47,47,47,34,34,34,47,34,47,34,34,47,34,47,34,47,34,47,34,34,47,47,34,47,47,47,34,47,47,47,47,47,47,34,47,34,34,47,34,34,34,34,47,47,34,47,34,34,34,34,47,34,34,47,34,34,34,47,34,47,47,34,34,34,47,47,47,34,34,34,34,34,47,47,34,47,47,34,47,47,34,34,34,34,34,34,34,34,47,34,47,47,47,34,34,34,47,47,47,34,47,47,47,47,47,47,47,34,34,47,47,34,34,34,34,34,34,47,47,34,34,34,47,34,47,34,34,34,47,47,47,47,47,47,34,34,47,34,47,34,47,34,34,47,34,47,34,34,47,47,47,47,34,34,47,34,47,47,47,47,34,34,47,34,34,34,34,47,47,34,34,47,47,47,47,34,47,34,47,47,34,34,34,34,47,34,34,34,47,34,34,47,47,34,34,47,34,34,34,47,47,34,47,34,47,47,34,47,34,34,34,34,47,47,47,34,47,47,34,47,34,34,34,47,34,34,34,34,34,47,47,47,47,47,34,47,34,47,47,47,47,34,34,34,47,47,34,34,34,47,47,47,34,34,34,47,34,34,47,47,47,47,34,34,47,47,34,47,47,47,47,34,47,34,34,34,47,47,47,34,47,47,47,47,34,47,47,47,34,34,34,47,34,34,34,47,34,34,47,34,47,47,34,47,47,34,34,34,47,34,47,47,34,34,34,47,34,47,47,34,34,47,47,34,47,34,47,47,47,47,47,34,47,34,34,47,47,34,34,47,47,47,47,34,47,34,34,34,47,34,47,34,47,34,47,47,47,34,34,34,47,47,34,47,34,34,47,47,47,47,34,47,47,47,34,47,47,47,47,47,34,34,47,34,34,47,34,47,34,34,47,47,34,34,47,47,34,34,34,47,47,47,34,34,34,34,34,47,34,47,34,47,47,47,34,47,47,47,34,47,34,34,47,34,34,47,34,47,47,34,47,47,47,47,34,34,47,34,34,47,34,34,34,34,47,47,47,34,47,34,47,47,47,34,34,34,47,34,47,47,47,47,47,47,47,47,34,47,47,47,34,34,47,47,47,34,34,47,34,34,47,47,34,47,34,34,47,47,47,34,47,47,47,47,34,34,47,34,34,34,34,47,34,47,34,47,34,34,34,34,47,34,34,47,34,34,34,47,34,47,47,34,47,34,34,34,34,47,47,47,47,47,47,47,47,47,47,34,34,47,47,47,34,47,47,34,34,34,47,34,34,47,34,34,34,34,34,47,47,47,34,47,47,34,34,34,34,34,47,34,47,47,34,34,34,47,34,34,47,47,47,47,34,34,34,34,47,47,47,34,47,34,34,34,47,47,34,34,47,34,47,47,34,47,47,34,34,34,34,47,34,34,34,34,47,47,34,34,34,34,34,34,34,34,34,34,34,34,34,47,34,47,34,34,34,47,47,47,34,47,34,47,47,47,47,34,34,47,47,47,34,47,34,34,34,47,34,47,47,47,34,47,47,34,47,47,34,47,34,34,47,34,34,47,47,47,34,34,47,34,47,34,47,47,47,34,47,47,34,47,47,34,47,47,47,34,34,47,47,34,34,47,47,34,47,34,47,34,34,34,34,47,34,47,47,47,47,47,34,47,47,34,34,47,34,34,47,47,47,47,47,47,34,47,34,34,47,34,34,34,47,47,34,47,47,47,47,47,34,47,34,47,47,34,34,34,47,34,34,47,34,34,47,34,34,34,47,34,34,34,34,47,34,47,34,47,47,47,47,47,34,34,34,47,47,34,34,34,47,34,34,34,47,34,34,34,34,34,47,34,34,34,47,47,47,34,47,34,47,34,34,47,47,34,34,34,47,34,47,47,47,47,47,34,47,47,34,47,47,34,47,47,47,34,47,47,47,47,47,34,47,34,34,34,47,34,34,47,34,47,34,47,34,47,47,34,47,47,47,34,34,34,34,34,34,34,47,34,34,34,34,34,47,47,47,34,34,47,34,34,47,34,34,47,47,47,34,34,47,47,47,47,34,47,47,47,34,34,47,47,34,34,47,47,34,34,47,47,47,47,47,34,34,47,47,34,47,47,47,34,34,34,47,34,47,34,47,34,34,34,47,34,47,47,47,34,34,34,47,34,47,47,34,34,34,47,34,34,47,47,34,47,47,47,47,34,47,47,34,34,34,47,34,47,34,47,47,47,34,34,47,34,47,47,47,47,34,47,47,47,47,34,34,34,34,47,47,47,47,34,47,34,47,34,34,34,47,47,34,47,34,34,34,34,34,34,34,47,47,47,47,47,34,34,34,47,34,34,34,34,34,34,34,34,34,47,34,34,34,47,34,34,47,47,34,34,47,34,47,34,47,47,47,34,47,47,47,34,47,34,47,47,47,34,34,34,34,47,34,34,34,34,34,34,47,47,34,34,47,34,47,47,34,34,34,47,47,47,47,34,34,47,47,34,34,34,34,34,34,34,34,47,34,47,47,34,47,34,47,47,47,47,34,47,47,47,34,47,34,34,47,47,34,34,47,47,34,34,34,34,47,47,34,47,34,47,47,47,34,34,34,47,47,34,34,34,47,47,47,47,47,47,47,47,34,47,34,47,47,47,34,34,47,34,34,47,34,34,34,47,47,47,34,34,34,47,34,47,34,47,47,34,47,47,47,34,34,34,47,34,34,47,34,47,34,34,34,34,34,34,47,47,34,34,34,34,34,34,47,47,47,47,34,47,47,34,47,47,47,47,34,34,34,34,34,34,47,34,34,47,47,34,47,47,34,47,47,47,34,34,34,34,47,47,34,34,47,47,47,34,34,47,47,34,34,47,47,34,47,34,47,47,47,47,34,47,47,34,47,34,34,47,47,47,47,47,34,34,47,47,47,34,34,47,34,47,47,47,34,34,47,47,47,34,47,47,47,34,34,47,47,47,47,47,34,47,47,34,47,34,34,34,47,34,34,47,34,47,47,47,34,34,47,47,47,34,47,34,47,34,47,47,47,34,47,34,47,47,34,47,47,34,47,47,47,34,47,34,47,47,47,47,47,47,47,34,47,47,47,47,47,34,34,34,47,34,47,34,47,34,34,34,47,47,34,47,47,47,47,34,34,34,34,34,34,47,34,34,34,47,47,34,34,34,34,47,47,47,47,34,34,47,47,34,47,47,34,34,47,47,34,47,34,47,47,47,47,47,34,34,34,34,34,47,47,34,34,34,34,47,34,47,34,34,47,47,47,34,34,34,34,47,47,34,47,34,34,34,34,34,47,47,34,47,34,47,47,47,34,47,34,47,47,34,47,47,34,34,47,47,34,34,47,34,34,34,34,34,34,47,47,34,34,34,34,34,47,47,34,47,47,47,47,47,34,34,34,47,47,34,47,34,47,47,34,34,47,34,34,34,47,34,47,34,47,34,34,47,34,47,47,34,47,34,47,34,34,34,47,34,47,47,34,47,34,34,34,34,34,47,34,34,47,34,34,34,47,47,34,47,34,34,47,47,47,47,47,47,34,34,47,47,47,34,47,47,47,34,47,47,47,34,34,47,34,47,34,47,34,47,47,34,34,47,47,47,47,47,34,47,34,47,34,47,47,47,47,47,34,47,47,47,34,47,47,47,34,34,47,34,34,47,47,34,34,47,34,34,34,34,34,34,34,34,47,47,47,47,47,34,34,47,47,34,34,47,34,47,34,47,34,34,34,34,34,34,34,47,47,47,34,47,34,47,34,34,34,34,47,47,34,34,34,47,34,47,34,34,47,34,34,47,47,34,34,47,34,34,34,34,34,34,47,47,47,34,47,47,34,47,47,34,47,47,47,47,34,47,47,34,34,47,34,34,34,47,47,34,34,34,34,34,34,47,34,47,47,47,34,47,47,34,47,47,47,47,34,47,47,34,47,47,47,47,34,47,34,34,34,34,47,47,34,47,34,47,34,34,47,47,47,34,47,47,34,34,47,47,34,34,47,47,34,47,47,47,34,34,34,34,34,47,34,47,47,34,47,34,47,47,34,34,47,34,47,34,47,47,47,34,34,47,47,47,47,34,47,47,47,34,34,47,34,34,34,34,47,34,34,34,47,34,34,47,34,34,34,47,47,34,34,34,34,34,34,34,34,34,34,47,47,47,34,47,34,47,47,34,47,34,47,34,34,47,47,34,47,34,47,34,34,47,34,47,34,34,34,34,34,34,47,47,47,47,47,47,47,34,47,34,34,34,47,34,34,34,34,34,47,34,47,34,34,47,34,34,47,47,47,34,34,47,34,47,34,34,34,34,34,47,47,34,47,47,34,34,34,47,47,47,47,47,34,34,34,34,47,47,47,34,47,34,47,34,34,34,34,34,34,47,47,47,34,34,34,34,47,47,47,34,47,34,34,34,47,47,47,47,34,34,34,34,47,34,47,47,34,47,34,47,34,47,34,34,47,47,34,47,34,47,47,47,47,34,34,34,47,34,47,34,47,34,47,47,47,34,47,47,34,47,47,34,34,47,34,47,34,47,47,47,34,47,47,47,47,34,47,34,34,47,47,34,47,34,47,47,47,47,34,34,47,34,34,47,47,47,34,34,47,34,34,34,34,34,34,47,47,34,34,47,47,47,47,47,34,34,34,34,34,34,47,34,47,47,47,47,47,34,34,34,34,34,34,34,34,47,34,34,34,47,47,34,34,47,34,34,34,47,34,47,47,34,34,47,34,34,47,34,47,47,47,34,47,47,47,47,34,34,34,47,34,47,34,47,34,47,34,34,34,47,34,34,47,34,47,47,34,34,47,47,47,34,47,47,34,34,47,34,34,47,34,47,47,34,34,47,34,47,34,47,34,34,34,34,47,34,34,34,34,34,34,34,47,34,34,47,47,47,47,47,47,34,47,47,34,47,47,47,47,34,34,47,47,47,34,34,47,34,47,47,34,34,34,47,47,34,47,34,47,34,34,34,34,34,34,34,47,47,47,47,34,47,47,34,34,47,47,47,34,34,47,34,47,47,47,47,34,47,34,34,34,47,47,34,34,34,47,34,34,34,34,47,47,34,34,47,47,47,34,47,34,34,34,47,34,34,34,34,34,34,34,34,34,34,34,47,47,47,47,34,47,47,34,47,34,47,47,34,47,34,47,34,47,34,34,34,34,34,34,34,47,34,34,34,47,34,34,34,47,47,47,47,34,34,34,34,47,34,34,47,34,34,47,34,34,47,47,47,34,34,34,47,47,34,34,34,47,34,34,47,34,34,47,34,47,47,47,34,34,34,47,34,47,34,47,47,47,47,34,47,34,34,34,47,47,34,47,34,47,34,34,47,47,47,47,34,47,34,47,34,47,47,34,47,34,47,34,47,47,47,47,34,47,47,47,34,47,34,34,47,34,47,47,47,47,34,34,34,47,34,34,47,47,47,47,34,47,34,47,34,34,47,34,34,47,34,34,47,34,34,47,47,47,47,47,47,34,47,47,47,47,47,47,34,34,34,34,47,34,34,34,34,34,34,34,34,47,34,34,47,34,34,47,47,47,34,47,34,47,47,47,34,34,34,34,47,47,47,47,34,47,47,47,47,34,47,47,34,47,34,34,47,47,47,34,47,34,47,47,47,34,47,47,34,34,34,34,47,47,47,34,34,47,47,47,34,47,34,47,47,47,47,47,34,34,47,34,34,34,34,47,34,34,34,34,34,47,47,47,34,34,34,34,47,47,34,34,47,47,47,34,34,34,47,47,47,34,47,47,34,34,34,47,47,47,47,47,47,34,34,47,47,47,47,34,47,34,34,34,47,47,47,47,34,34,34,34,47,34,47,47,47,47,34,47,47,34,34,47,34,34,47,47,34,34,47,34,47,34,34,34,34,34,34,47,47,47,47,47,34,47,47,34,34,34,34,34,47,47,34,47,47,34,47,47,34,47,34,47,47,47,47,47,47,34,47,34,34,34,34,47,47,34,47,34,34,47,34,34,47,47,47,34,34,34,47,34,34,47,47,34,34,34,47,34,34,34,34,34,34,34,34,34,47,47,34,47,34,34,34,34,34,34,47,47,47,47,47,47,47,34,34,34,47,47,34,34,47,34,47,34,34,47,47,47,47,47,34,47,34,34,34,34,34,34,47,47,47,47,47,34,47,34,34,34,47,34,47,34,47,34,34,47,47,34,34,47,34,47,34,34,47,34,47,47,47,34,34,47,47,34,34,34,34,34,34,47,34,34,47,47,47,47,34,34,34,47,34,34,47,34,34,34,47,34,34,34,47,34,34,34,47,34,47,47,34,47,34,47,47,47,34,47,47,34,47,47,34,34,47,47,34,47,34,47,34,34,34,34,47,47,34,34,34,47,34,34,47,47,34,34,34,34,34,47,47,47,34,47,47,34,34,47,34,34,47,34,34,34,34,34,47,47,34,34,47,34,34,47,34,34,34,47,34,34,47,34,34,47,34,47,47,34,47,34,47,34,47,47,34,34,47,47,47,47,47,34,47,47,34,47,34,47,47,34,34,34,34,47,47,34,47,47,34,47,34,47,47,47,47,47,34,34,34,34,34,47,34,47,34,34,47,34,34,34,47,47,47,47,34,47,47,34,47,47,47,34,47,47,47,34,34,47,34,47,34,34,34,34,34,47,34,47,47,47,34,47,47,47,34,47,47,34,47,47,47,47,34,34,34,47,47,47,34,47,47,34,47,34,34,34,47,47,47,34,34,34,47,47,34,34,34,47,34,34,34,47,47,34,47,34,34,47,47,34,47,47,47,34,47,34,34,47,34,34,34,47,34,34,34,34,34,34,47,34,34,34,47,47,47,34,47,47,34,47,47,34,47,34,47,47,47,34,34,34,34,47,34,34,47,47,34,34,47,47,47,47,47,34,47,34,47,47,34,34,47,34,47,47,34,34,34,47,34,47,34,34,47,34,47,47,34,34,34,47,47,47,47,34,47,47,47,34,34,47,34,34,47,47,47,47,47,34,34,34,34,34,47,34,47,34,34,34,34,34,47,34,47,34,47,47,47,34,47,47,34,34,47,34,47,34,34,34,34,34,47,34,47,47,47,34,47,34,34,34,34,34,34,47,47,34,34,34,47,47,34,34,34,47,47,47,47,34,34,34,47,47,34,47,34,34,47,47,34,47,34,47,34,47,47,47,34,47,47,47,47,34,47,47,47,34,47,47,34,34,47,34,34,47,47,47,47,47,47,47,34,34,34,47,34,47,34,47,47,47,47,34,34,47,34,34,47,47,47,34,34,47,47,47,47,47,34,47,47,47,47,47,47,34,34,47,34,34,34,47,47,47,34,34,47,34,47,47,47,47,34,47,34,47,34,34,34,47,47,47,47,34,34,34,34,47,47,47,47,47,47,47,34,34,47,34,34,34,47,47,34,47,47,47,34,47,34,34,47,47,34,47,34,34,34,47,47,47,47,34,34,34,47,47,47,47,34,34,47,34,47,47,34,34,47,47,34,34,34,34,47,34,34,34,34,47,47,34,34,47,47,47,34,34,47,47,34,34,47,47,34,34,34,47,34,34,47,47,47,47,34,47,34,34,34,34,47,34,47,34,34,47,47,47,34,47,47,34,47,34,47,34,47,47,47,34,47,47,47,47,34,34,34,34,34,34,47,34,47,47,47,47,47,34,47,47,47,34,47,34,47,47,47,34,47,34,47,47,34,47,47,34,34,47,34,47,47,34,34,34,47,47,34,34,34,34,47,34,47,47,47,34,47,34,34,34,34,47,47,34,47,47,47,34,34,47,47,47,34,47,34,47,34,47,34,34,34,47,34,47,34,34,47,34,34,34,47,34,34,47,34,47,47,34,47,34,34,47,34,34,47,47,34,47,34,47,47,47,47,47,47,34,47,34,47,34,47,34,34,34,34,47,34,34,47,34,34,47,34,34,47,47,34,47,34,34,47,47,34,34,34,34,47,47,47,47,34,47,34,34,47,34,34,47,47,34,47,34,34,47,34,47,47,34,47,47,34,47,47,34,34,47,47,34,34,47,47,34,47,34,47,34,34,34,34,47,47,47,34,47,47,34,34,47,34,47,47,47,47,34,47,34,34,34,47,47,47,34,47,34,34,47,34,47,34,34,47,34,47,47,34,47,34,34,47,34,34,34,47,47,34,34,47,47,34,34,47,34,47,34,34,47,34,34,47,47,47,34,34,34,34,34,47,34,34,34,34,47,47,34,34,34,34,34,47,47,47,34,47,34,47,34,47,34,34,47,34,47,47,34,34,47,34,34,34,34,34,34,34,34,34,34,47,47,34,47,34,34,34,34,34,47,34,34,47,34,34,47,34,34,47,47,34,47,47,34,34,34,34,34,34,34,34,34,34,34,34,47,34,47,47,47,34,47,34,34,47,34,34,34,34,34,34,47,47,47,34,47,47,34,34,34,47,34,34,34,47,47,47,34,47,47,34,34,34,47,34,34,34,34,47,34,47,47,34,47,34,34,47,47,47,47,47,34,34,34,34,34,47,47,47,34,47,34,34,47,34,47,47,34,34,34,47,47,34,47,47,34,47,47,47,47,47,47,47,34,34,47,34,34,34,47,47,34,47,47]
    print(s.dailyTemperatures(numbers))

if __name__ == '__main__':
    main()