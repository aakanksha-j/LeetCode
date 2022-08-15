class Solution:
    """Approach 1:
       Time complexity: O(n)
       Space complexity: O(1)
       Runtime: 44 ms
       Memory: 14.2 MB
    """
    def intToRoman(self, num: int) -> str:
        op = ''
        while num > 0:
            if num >= 1000:
                op = op + 'M'
                num -= 1000
            elif num >= 900:
                op = op + 'CM'
                num -= 900
            elif num >= 500:
                op = op + 'D'
                num -= 500
            elif num >= 400:
                op = op + 'CD'
                num -= 400
            elif num >= 100:
                op = op + 'C'
                num -= 100
            elif num >= 90:
                op = op + 'XC'
                num -= 90
            elif num >= 50:
                op = op + 'L'
                num -= 50
            elif num >= 40:
                op = op + 'XL'
                num -= 40
            elif num >= 10:
                op = op + 'X'
                num -= 10
            elif num >= 9:
                op = op + 'IX'
                num -= 9
            elif num >= 5:
                op = op + 'V'
                num -= 5
            elif num >= 4:
                op = op + 'IV'
                num -= 4
            elif num >= 1:
                op = op + 'I'
                num -= 1

        return op

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
