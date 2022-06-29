# 1. own solution using stack and dictionary
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # time: O(n) - for loop to iterate over tokens list
        # space: O(n) - extra space for stack, worst case - stack may have all numbers at same time

        stack = []

        operators = {'+': 1, '-': 2, '*': 3, '/': 4} # dic not needed, refer 3rd

        for i in range(len(tokens)): # token in tokens
            if tokens[i] in operators:
                num2 = int(stack.pop()) # int not needed if used while appending
                num1 = int(stack.pop())
                if operators[tokens[i]] == 1:
                    stack.append(num1 + num2)
                elif operators[tokens[i]] == 2:
                    stack.append(num1 - num2)
                elif operators[tokens[i]] == 3:
                    stack.append(num1 * num2)
                elif operators[tokens[i]] == 4:
                    stack.append(num1 / num2)

            else:
                stack.append(tokens[i]) # int(tokens[i])

        return int(stack[-1]) # stack.pop()


# 2. leetcode solution using stack, and dictionary with lambdas

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # leetcode solution - stack using lambdas

        stack = []

        operators = {'+': lambda a, b: a + b,
                     '-': lambda a, b: a - b,
                     '*': lambda a, b: a * b,
                     '/': lambda a, b: int(a / b)
                    }

        for token in tokens:
            if token in operators:
                num2 = stack.pop()
                num1 = stack.pop()
                operation = operators[token]
                stack.append(operation(num1, num2))
            else:
                stack.append(int(token))

        return stack.pop()

# 3. leetcode solution - stack without lambdas, dictionary for operators
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:
            if token not in '+-*/':
                stack.append(int(token))
                continue

            num2 = stack.pop()
            num1 = stack.pop()

            if token == '+':
                stack.append(num1 + num2)
            elif token == '-':
                stack.append(num1 - num2)
            elif token == '*':
                stack.append(num1 * num2)
            else:
                stack.append(int(num1 / num2))

        return stack.pop()
