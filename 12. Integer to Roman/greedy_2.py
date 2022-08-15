class Solution:
    """Approach 1:
       Time complexity: O(n)
       Space complexity: O(1)
       Runtime: 84 ms
       Memory: 14.1 MB
    """
    def intToRoman(self, num: int) -> str:
        digits = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        output = []
        root = num
        for value, symbol in digits:
            if root <= 0: break
            if root >= value:
                count, root = divmod(root, value) # returns quotient and remainder
                print(count, root)
                output.append(count*symbol)
        return ''.join(output)

def main():
    numbers = 3999
    s=Solution()
    print(s.intToRoman(numbers))
    numbers = 1994
    print(s.intToRoman(numbers))
    numbers = 58
    print(s.intToRoman(numbers))

if __name__ == '__main__':
    main()
